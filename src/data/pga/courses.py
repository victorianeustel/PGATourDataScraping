from .api import PGA_API
import requests

def get_course_stat_details(year: int):
    data = {
        "operationName": "CourseStatsDetails",
        "variables": {
            "tourCode": "R",
            "queryType": "TOUGHEST_COURSE",
            "round": "ALL",
            "year": year
        },
        "query": "query CourseStatsDetails($tourCode: TourCode!, $queryType: CourseStatsId!, $round: ToughestRound, $year: Int) {\n  courseStatsDetails(\n    tourCode: $tourCode\n    queryType: $queryType\n    round: $round\n    year: $year\n  ) {\n    tourCode\n    year\n    round\n    displayYear\n    seasons {\n      year\n      displaySeason\n    }\n    headers\n    displayName\n    tableName\n    rows {\n      rank\n      displayName\n      values {\n        value\n        tendency\n      }\n      tournamentId\n      tournamentName\n    }\n    shareURL\n    roundPills {\n      display\n      queryVal\n    }\n  }\n}"
    }
    
    response = requests.post(PGA_API.url, headers=PGA_API.headers, json=data)
    return response.json()

def get_course_stat_overviews(year: int):
    data = {
        "operationName": "CourseStatsOverview",
        "variables": {
            "tourCode": "R",
            "year": year
        },
        "query": "query CourseStatsOverview($tourCode: TourCode!, $year: Int) {\n  courseStatsOverview(tourCode: $tourCode, year: $year) {\n    tourCode\n    year\n    categories {\n      header\n      detailId\n      items {\n        displayName\n        rank\n        image\n        details {\n          value\n          label\n        }\n      }\n    }\n  }\n}"
    }
    
    response = requests.post(PGA_API.url, headers=PGA_API.headers, json=data)
    return response.json()