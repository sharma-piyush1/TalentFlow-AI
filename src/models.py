from pydantic import BaseModel, Field
from typing import List

class Candidate(BaseModel):
    name: str = Field(..., description="Full name of the candidate")
    profile_url: str = Field(..., description="URL to LinkedIn, GitHub, or Portfolio")
    skills: str = Field(..., description="List of relevant technical skills found")
    score: int = Field(..., description="Relevance score from 0 to 10")
    reasoning: str = Field(..., description="Short explanation of why this score was given")

class CandidateList(BaseModel):
    candidates: List[Candidate] = Field(..., description="List of analyzed candidates")