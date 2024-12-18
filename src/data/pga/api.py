import os
from dotenv import load_dotenv

class PGA_API:
    load_dotenv()
    
    api_key = os.environ.get('PGA_TOUR_API_KEY')

    url = "https://orchestrator.pgatour.com/graphql"
    headers = {
        "content-type": "application/json",
        "priority": "u=1, i",
        "x-api-key": api_key,
    }