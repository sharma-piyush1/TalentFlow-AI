import os 
from crewai import Crew, Process
from agents import RecruitmentAgents
from tasks import RecruitmentTasks
from dotenv import load_dotenv

# 1. Load Environment variables 
load_dotenv()

def run():
    # 2. Define JD for test
    job_description = """
    Role: Senior Python Developer
    Location: Remote / Bhopal
    Skills Required: Python, FastAPI, Docker, LangChain.
    Experience: 3-5 Years.
    Responsibilities: Build scalable AI agents and backend systems.
    """

    print(f"Starting Recruitment Crew for JD:\n{job_description}\n")

    # 3. Initializing the classes
    agents = RecruitmentAgents()
    tasks = RecruitmentTasks()

    # 4. Hiring Agents (Initiating)
    researcher = agents.researcher_agent()
    profiler = agents.profiler_agent()
    writer = agents.writer_agent()

    # 5. Assigning Tasks
    # Note: We pass the previous task object in a list [task1] to the context argument
    task1 = tasks.sourcing_task(researcher, job_description)
    task2 = tasks.profiling_task(profiler, [task1]) 
    task3 = tasks.writing_task(writer, [task2]) 

    # 6. Make CrewAI (Team assembly)
    crew = Crew(
        agents=[researcher, profiler, writer],
        tasks=[task1, task2, task3],
        verbose=True, # This will show in terminal what is happening
        process=Process.sequential # One after another work
    )

    # 7. Mission Start!
    result = crew.kickoff()
    
    print("\n\n########################")
    print("## HERE IS THE RESULT ##")
    print("########################\n")
    print(result)

    print("\n\n-----------------------------------------------")
    print("✅ Emails have been saved to 'candidates_outreach.md'")
    print("-----------------------------------------------")

if __name__ == "__main__":
    run()