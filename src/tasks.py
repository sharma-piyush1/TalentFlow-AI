from crewai import Task
from models import CandidateList 

class RecruitmentTasks:

    def sourcing_task(self, agent, job_description):
        return Task(
            description=(
                f"Conduct a targeted search for candidates based on this JD:\n{job_description}\n\n"
                "1. Search specifically for candidates in 'Bhopal' first. If none found, look for 'Remote'.\n"
                "2. Look for key skills: Python, FastAPI, Docker, LangChain.\n"
                "3. Collect Name, Profile URL, and Key Skills for at least 3 candidates."
            ),
            expected_output="A list of potential candidates with Names, URLs, and Skills.",
            agent=agent
        )

    def profiling_task(self, agent, context_tasks):
        return Task(
            description=(
                "Analyze the list of candidates found by the researcher.\n"
                "1. Verify if they match the skills (Python, FastAPI, Docker, LangChain).\n"
                "2. Score each candidate (0-10).\n"
                "3. IMPORTANT: Return the result as a structured JSON object."
            ),
            expected_output="A structured list of candidates with scores.",
            agent=agent,
            context=context_tasks,
            output_pydantic=CandidateList # <--- THIS FORCES STRUCTURED DATA
        )

    def writing_task(self, agent, formatted_candidates_info):
        # This task now takes text input (stringified list) because we will filter it first
        return Task(
            description=(
                f"Draft personalized outreach emails for these approved candidates:\n{formatted_candidates_info}\n\n"
                "1. The email should be professional but engaging.\n"
                "2. Mention specific skills from their profile.\n"
                "3. Include a call to action."
            ),
            expected_output="A formatted text containing emails.",
            agent=agent
        )