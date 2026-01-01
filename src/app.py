import streamlit as st
import pandas as pd
import os
import sys

# --- FIX START: Add 'src' to the system path ---
# This tells Python to look inside the 'src' folder for imports
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
# --- FIX END ---

from dotenv import load_dotenv
from crewai import Crew, Process
# Now these imports will work because Python knows to look in 'src'
from agents import RecruitmentAgents
from tasks import RecruitmentTasks

load_dotenv()

st.set_page_config(page_title="TalentFlow AI", page_icon="🚀", layout="wide")

st.title("🚀 TalentFlow: AI Recruitment Engine")
st.markdown("Search -> **Review** -> Email. You verify the candidates before we write to them.")

# Initialize Session State
if "candidates_data" not in st.session_state:
    st.session_state.candidates_data = None
if "emails_generated" not in st.session_state:
    st.session_state.emails_generated = False

# Sidebar for Job Description
with st.sidebar:
    st.header("1. Job Details")
    job_description = st.text_area(
        "Paste JD Here:", 
        value="Senior Python Developer (Remote/Bhopal). Skills: Python, FastAPI, Docker, LangChain. Exp: 3-5 Years.",
        height=300
    )
    start_search = st.button("🔍 Find & Score Candidates")

# --- STAGE 1: SEARCH & PROFILE ---
if start_search:
    with st.spinner('Agents are scouring the web and scoring profiles... (This takes 1-2 minutes)'):
        try:
            # Init Agents & Tasks
            agents = RecruitmentAgents()
            tasks = RecruitmentTasks()
            
            researcher = agents.researcher_agent()
            profiler = agents.profiler_agent()

            # Create the Search Crew (No Writer yet)
            task1 = tasks.sourcing_task(researcher, job_description)
            task2 = tasks.profiling_task(profiler, [task1])

            crew_1 = Crew(
                agents=[researcher, profiler],
                tasks=[task1, task2],
                verbose=True,
                max_rpm=20 # Limit to avoid 429 errors
            )

            result = crew_1.kickoff()
            
            # Handle Pydantic Output
            candidate_list = result.pydantic.dict()['candidates']
            st.session_state.candidates_data = candidate_list
            st.session_state.emails_generated = False 

        except Exception as e:
            st.error(f"Error during search: {e}")

# --- STAGE 2: HUMAN REVIEW ---
if st.session_state.candidates_data:
    st.header("2. Review Candidates")
    st.info("Check the boxes of candidates you want to contact. You can also edit their details directly in the table.")
    
    # Convert to DataFrame
    df = pd.DataFrame(st.session_state.candidates_data)
    
    if "Select" not in df.columns:
        df.insert(0, "Select", True)

    # Show Editable Table
    edited_df = st.data_editor(
        df,
        column_config={
            "profile_url": st.column_config.LinkColumn("Profile URL"),
            "score": st.column_config.ProgressColumn("Match Score", min_value=0, max_value=10, format="%d/10"),
        },
        hide_index=True,
        use_container_width=True
    )

    # --- STAGE 3: GENERATE EMAILS ---
    st.divider()
    col1, col2 = st.columns([1, 4])
    with col1:
        generate_emails = st.button("✍️ Write Emails")
    
    with col2:
        csv = edited_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="💾 Download CSV",
            data=csv,
            file_name="shortlisted_candidates.csv",
            mime="text/csv",
        )

    if generate_emails:
        selected_candidates = edited_df[edited_df["Select"] == True]
        
        if selected_candidates.empty:
            st.warning("Please select at least one candidate!")
        else:
            with st.spinner("Writer Agent is drafting emails..."):
                try:
                    candidates_string = selected_candidates.to_json(orient="records")
                    
                    agents = RecruitmentAgents()
                    tasks = RecruitmentTasks()
                    writer = agents.writer_agent()
                    
                    task3 = tasks.writing_task(writer, candidates_string)
                    
                    crew_2 = Crew(
                        agents=[writer],
                        tasks=[task3],
                        verbose=True
                    )
                    
                    email_result = crew_2.kickoff()
                    
                    st.success("Emails Drafted Successfully!")
                    st.subheader("📬 Final Outreach Emails")
                    st.markdown(email_result)
                except Exception as e:
                    st.error(f"Error generating emails: {e}")