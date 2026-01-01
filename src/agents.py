import os
from dotenv import load_dotenv
from crewai import Agent, LLM
from tools import find_candidates 

load_dotenv()

# --- GEMINI IMPOSTER SETUP ---
os.environ["OPENAI_API_KEY"] = os.getenv("GOOGLE_API_KEY")
os.environ["OPENAI_API_BASE"] = "https://generativelanguage.googleapis.com/v1beta/openai/"
os.environ["OPENAI_MODEL_NAME"] = "gemini-3-flash-preview"

llm = LLM(
    model="openai/gemini-3-flash-preview",
    api_key=os.getenv("GOOGLE_API_KEY")
)

class RecruitmentAgents:
    
    def researcher_agent(self):
        return Agent(
            role='Senior Tech Sourcer',
            goal='Find REAL, VERIFIABLE candidate profiles. Do not invent people.',
            verbose=True,
            memory=True,
            backstory=(
                "You are an expert tech sourcer. You verify that every candidate exists."
                "CRITICAL RULE: You must ONLY use profiles returned by the 'find_candidates' tool."
                "If the tool returns no results, try a different search query."
                "NEVER make up names or URLs. If a URL looks like 'example.com' or 'linkedin.com/in/name-placeholder', IT IS WRONG."
            ),
            tools=[find_candidates],
            llm=llm,
            allow_delegation=False # Disabled delegation to force it to search itself
        )

    def profiler_agent(self):
        return Agent(
            role='Candidate Profiler',
            goal='Analyze extracted profiles and rank them',
            verbose=True,
            memory=True,
            backstory=("You are a meticulous HR Specialist who checks if profiles are real and skilled."),
            tools=[], 
            llm=llm,
            allow_delegation=False
        )

    def writer_agent(self):
        return Agent(
            role="Outreach Specialist",
            goal='Draft personalized outreach emails',
            verbose=True,
            memory=True,
            backstory=("You are a copywriter for recruitment."),
            tools=[],
            llm=llm,
            allow_delegation=False
        )