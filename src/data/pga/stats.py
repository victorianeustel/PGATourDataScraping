from .api import PGA_API
import requests

def get_stats_overview(year: int):
    data = {
        "operationName":"StatOverview",
        "variables":{
            "tourCode": "R",
            "year": year
        },
        "query": "query StatOverview($tourCode: TourCode!, $year: Int) {\n  statOverview(tourCode: $tourCode, year: $year) {\n    tourCode\n    year\n    categories {\n      category\n      displayName\n      subCategories {\n        displayName\n        stats {\n          statId\n          statTitle\n        }\n      }\n      categoryType\n    }\n    stats {\n      statName\n      tourAvg\n      statId\n      players {\n        statId\n        playerId\n        statTitle\n        statValue\n        playerName\n        rank\n        country\n        countryFlag\n      }\n    }\n  }\n}"        
        }

    response = requests.post(PGA_API.url, headers=PGA_API.headers, json=data)
    return response.json()

