from .api import PGA_API
import requests

def get_course_stats(tournamentId: str):
    data = {
        "operationName": "CourseStats",
        "variables": {
            "tournamentId": tournamentId
        },
        "query": "query CourseStats($tournamentId: ID!) {\n  courseStats(tournamentId: $tournamentId) {\n    ...CourseStatsFragment\n  }\n}\n\nfragment CourseStatsFragment on TournamentHoleStats {\n  tournamentId\n  courses {\n    tournamentId\n    courseId\n    courseName\n    courseCode\n    holeDetailsAvailability\n    par\n    yardage\n    hostCourse\n    courseImage\n    roundHoleStats {\n      roundHeader\n      roundNum\n      live\n      holeStats {\n        ... on CourseHoleStats {\n          __typename\n          courseHoleNum\n          parValue\n          yards\n          scoringAverage\n          scoringAverageDiff\n          scoringDiffTendency\n          eagles\n          birdies\n          pars\n          bogeys\n          doubleBogey\n          rank\n          holeImage\n          live\n          holePickleGreenLeftToRight\n          pinGreen {\n            leftToRightCoords {\n              x\n              y\n              z\n            }\n            bottomToTopCoords {\n              x\n              y\n              z\n            }\n          }\n        }\n        ... on SummaryRow {\n          __typename\n          rowType\n          par\n          scoringAverageDiff\n          scoringDiffTendency\n          yardage\n          scoringAverage\n          eagles\n          birdies\n          pars\n          bogeys\n          doubleBogey\n        }\n      }\n    }\n    courseOverview {\n      id\n      image\n      name\n      city\n      state\n      country\n      overview {\n        label\n        value\n        detail\n        secondaryDetail\n        wide\n        smallCopy\n      }\n    }\n    shotlinkLogo\n  }\n}"
    }
    response = requests.post(PGA_API.url, headers=PGA_API.headers, json=data)
    return response.json()

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