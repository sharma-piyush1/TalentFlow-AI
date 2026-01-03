import os
from crewai.tools import tool
from exa_py import Exa

@tool
def find_candidates(query: str) -> str:
    """
    Search for REAL candidate profiles. 
    INPUT: A search string like "Senior Python Developer linkedin" or "Python developer github".
    """
    # Initialize Exa
    exa = Exa(api_key=os.getenv("EXA_API_KEY"))
    
    try:
        # Perform the search
        # We added 'text=True' so the agent can read the profile summary.
        result = exa.search_and_contents(
            query,
            type="neural",
            num_results=5,
            text=True,  # This is crucial: Get the actual text of the profile
            category="personal"
        )
        return str(result)
        
    except Exception as e:
        return f"Error fetching search results: {str(e)}"