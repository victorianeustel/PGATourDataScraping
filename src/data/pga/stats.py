import urllib
from .api import PGA_API
import requests

def get_stats_overview(year: int, tourCode: str = "R"):
    data = {
        "operationName":"StatOverview",
        "variables":{
            "tourCode": tourCode,
            "year": year
        },
        "query": "query StatOverview($tourCode: TourCode!, $year: Int) {\n  statOverview(tourCode: $tourCode, year: $year) {\n    tourCode\n    year\n    categories {\n      category\n      displayName\n      subCategories {\n        displayName\n        stats {\n          statId\n          statTitle\n        }\n      }\n      categoryType\n    }\n    stats {\n      statName\n      tourAvg\n      statId\n      players {\n        statId\n        playerId\n        statTitle\n        statValue\n        playerName\n        rank\n        country\n        countryFlag\n      }\n    }\n  }\n}"        
        }

    response = requests.post(PGA_API.url, headers=PGA_API.headers, json=data)
    return response.json()


def get_stat_details(statId:str = "109", year:int = 2024, tourCode:str = "R"):
    data = {
        "operationName": "StatDetails",
        "variables": {
            "tourCode": tourCode,
            "statId": statId,
            "year": year,
            "eventQuery": None
        },
        "query": "query StatDetails($tourCode: TourCode!, $statId: String!, $year: Int, $eventQuery: StatDetailEventQuery) {\n  statDetails(\n    tourCode: $tourCode\n    statId: $statId\n    year: $year\n    eventQuery: $eventQuery\n  ) {\n    __typename\n    tourCode\n    year\n    displaySeason\n    statId\n    statType\n    tournamentPills {\n      tournamentId\n      displayName\n    }\n    yearPills {\n      year\n      displaySeason\n    }\n    statTitle\n    statDescription\n    tourAvg\n    lastProcessed\n    statHeaders\n    statCategories {\n      category\n      displayName\n      subCategories {\n        displayName\n        stats {\n          statId\n          statTitle\n        }\n      }\n    }\n    rows {\n      ... on StatDetailsPlayer {\n        __typename\n        playerId\n        playerName\n        country\n        countryFlag\n        rank\n        rankDiff\n        rankChangeTendency\n        stats {\n          statName\n          statValue\n          color\n        }\n      }\n      ... on StatDetailTourAvg {\n        __typename\n        displayName\n        value\n      }\n    }\n    sponsorLogo\n  }\n}"
    }
    
    response = requests.post(PGA_API.url, headers=PGA_API.headers, json=data)
    return response.json()

def get_stats_path(statsId: int, year: int, tourCode: str = 'R', timePeriod:str = 'THROUGH_EVENT'):
    params = {
        'timePeriod': timePeriod, 
        'statsId': statsId, 
        'tourCode': tourCode, 
        'year': year 
        }
    path = 'https://www.pgatour.com/api/stats-download?' + urllib.parse.urlencode(params)
    return path
