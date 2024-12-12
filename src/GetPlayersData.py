import requests

url = "https://orchestrator.pgatour.com/graphql"
headers = {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9",
    "content-type": "application/json",
    "priority": "u=1, i",
    "sec-ch-ua": "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "x-amz-user-agent": "aws-amplify/3.0.7",
    "x-api-key": "da2-gsrx5bibzbb4njvhl7t37wqyl4",
    "x-pgat-platform": "web"
}
    
def GetPlayerData(playerId: str):
    data = {
        "operationName":"PlayerProfileCareer",
        "variables":{
            "playerId": playerId,
            "tourCode":"R"
            },
        "query": "query PlayerProfileCareer($playerId: String!, $tourCode: TourCode) {\n  playerProfileCareer(playerId: $playerId, tourCode: $tourCode) {\n    playerId\n    tourCode\n    events\n    wins\n    winsTitle\n    internationalWins\n    majorWins\n    cutsMade\n    runnerUp\n    second\n    third\n    top10\n    top25\n    years {\n      cutsMade\n      displaySeason\n      events\n      officialMoney\n      second\n      standingsPoints\n      standingsRank\n      third\n      top10\n      top25\n      tourCode\n      wins\n      withdrawn\n      year\n    }\n    officialMoney\n    tourPills {\n      tourCode\n      displayName\n    }\n    achievements {\n      title\n      value\n    }\n    tables {\n      tableName\n      tableDetail\n      rows {\n        rowTitle\n        rowTitleDetail\n        rowContent\n        secondContent\n      }\n    }\n    years {\n      tourCode\n      displaySeason\n      year\n      events\n      wins\n      second\n      third\n      top10\n      top25\n      cutsMade\n      withdrawn\n      officialMoney\n      standingsPoints\n      standingsRank\n    }\n  }\n}"
        }

    response = requests.post(url, headers=headers, json=data)

    return response.json()

def GetStatsOverview(year: int):
    data = {
        "operationName":"StatOverview",
        "variables":{
            "tourCode": "R",
            "year": year
        },
        "query": "query StatOverview($tourCode: TourCode!, $year: Int) {\n  statOverview(tourCode: $tourCode, year: $year) {\n    tourCode\n    year\n    categories {\n      category\n      displayName\n      subCategories {\n        displayName\n        stats {\n          statId\n          statTitle\n        }\n      }\n      categoryType\n    }\n    stats {\n      statName\n      tourAvg\n      statId\n      players {\n        statId\n        playerId\n        statTitle\n        statValue\n        playerName\n        rank\n        country\n        countryFlag\n      }\n    }\n  }\n}"        
        }

    response = requests.post(url, headers=headers, json=data)

    return response.json()

def GetPlayerFullStatsOverview(playerId:str):
    data = {
        "operationName":"ProfileStatsFullV2",
        "variables":{
            "playerId": playerId
        },
        "query": "query ProfileStatsFullV2($playerId: ID!, $year: Int) {\n  playerProfileStatsFullV2(playerId: $playerId, year: $year) {\n    messages {\n      message\n    }\n    playerProfileStatsFull {\n      tour\n      season\n      displaySeason\n      categories {\n        category\n        displayTitle\n      }\n      topStats {\n        rank\n        value\n        statId\n        title\n        category\n        aboveOrBelow\n        fieldAverage\n      }\n      overview {\n        rank\n        value\n        title\n        statId\n        category\n        aboveOrBelow\n        rankDeviation\n        fieldAverage\n      }\n      stats {\n        statId\n        rank\n        value\n        title\n        category\n        aboveOrBelow\n        fieldAverage\n        supportingStat {\n          description\n          value\n        }\n        supportingValue {\n          description\n          value\n        }\n      }\n    }\n  }\n}"        }

    response = requests.post(url, headers=headers, json=data)

    return response.json()

def GetPlayerStatsYears(playerId:str):
    data = {
        "operationName":"PlayerProfileStatsYears",
        "variables":{
            "playerId": playerId
        },
        "query": 
        "query PlayerProfileStatsYears($playerId: ID!) {\n  playerProfileStatsYears(playerId: $playerId) {\n    year\n    season\n    tours\n  }\n}"
    }
    response = requests.post(url, headers=headers, json=data)

    return response.json()

def PlayerProfileStandings(playerId:str):
    data = {
        "operationName":"PlayerProfileStandings",
        "variables":{
            "playerId": playerId
        },
        "query": "query PlayerProfileStandings($playerId: ID!) {\n  playerProfileStandings(playerId: $playerId) {\n    tour\n    displaySeason\n    standings {\n      id\n      logo\n      logoDark\n      title\n      description\n      total\n      totalLabel\n      rank\n      rankLogo\n      owgr\n      totals {\n        total\n        totalLabel\n      }\n      detailUrl\n    }\n  }\n}"    }
    response = requests.post(url, headers=headers, json=data)

    return response.json()

def PlayerScorecards(playerId:str):
    data = {
        "operationName":"PlayerProfileScorecards",
        "variables":{
            "playerId": playerId
        },
        "query": "query PlayerProfileScorecards($playerId: ID!) {\n  playerProfileScorecards(playerId: $playerId) {\n    playerId\n    tours {\n      tourCode\n      years {\n        year\n        displayYear\n        tournamentPills {\n          tournamentId\n          displayName\n        }\n      }\n    }\n  }\n}"    }
    response = requests.post(url, headers=headers, json=data)

    return response.json()