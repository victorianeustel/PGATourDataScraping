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

def GetPlayerProfileStandings(playerId:str):
    data = {
        "operationName":"PlayerProfileStandings",
        "variables":{
            "playerId": playerId
        },
        "query": "query PlayerProfileStandings($playerId: ID!) {\n  playerProfileStandings(playerId: $playerId) {\n    tour\n    displaySeason\n    standings {\n      id\n      logo\n      logoDark\n      title\n      description\n      total\n      totalLabel\n      rank\n      rankLogo\n      owgr\n      totals {\n        total\n        totalLabel\n      }\n      detailUrl\n    }\n  }\n}"    }
    response = requests.post(url, headers=headers, json=data)

    return response.json()

def GetPlayerScorecards(playerId:str):
    data = {
        "operationName":"PlayerProfileScorecards",
        "variables":{
            "playerId": playerId
        },
        "query": "query PlayerProfileScorecards($playerId: ID!) {\n  playerProfileScorecards(playerId: $playerId) {\n    playerId\n    tours {\n      tourCode\n      years {\n        year\n        displayYear\n        tournamentPills {\n          tournamentId\n          displayName\n        }\n      }\n    }\n  }\n}"    }
    response = requests.post(url, headers=headers, json=data)

    return response.json()

def GetPlayerDirectory(playerId:str):
    data = {
        "operationName": "PlayerDirectory",
        "variables": {
            "tourCode": "R"
        },
        "query": "query PlayerDirectory($tourCode: TourCode!, $active: Boolean) {\n  playerDirectory(tourCode: $tourCode, active: $active) {\n    tourCode\n    players {\n      id\n      isActive\n      firstName\n      lastName\n      shortName\n      displayName\n      alphaSort\n      country\n      countryFlag\n      headshot\n      playerBio {\n        id\n        age\n        education\n        turnedPro\n      }\n    }\n  }\n}"
    }
    response = requests.post(url, headers=headers, json=data)

    return response.json()

def GetPlayer(playerId:str):
    data = {
        "operationName": "Player",
        "variables": {
            "playerId": "49303"
        },
        "query": "query Player($playerId: ID!) {\n  player(id: $playerId) {\n    bioLink\n    countryFlag\n    country\n    displayName\n    firstName\n    id\n    lastName\n    playerBio {\n      deceased\n      deceasedDate\n      age\n      birthplace {\n        countryCode\n        country\n        city\n        state\n        stateCode\n      }\n      born\n      bornAccessibilityText\n      degree\n      careerEarnings\n      family\n      graduationYear\n      heightImperial\n      heightImperialAccessibilityText\n      heightMeters\n      overview\n      personal\n      playsFrom {\n        city\n        country\n        countryCode\n        state\n        stateCode\n      }\n      pronunciation\n      residence {\n        city\n        country\n        state\n        countryCode\n        stateCode\n      }\n      school\n      social {\n        type\n        url\n      }\n      turnedPro\n      weightImperial\n      weightKilograms\n      websiteURL\n      exemptions {\n        tour\n        description\n        expirationDate\n      }\n    }\n    rank {\n      rank\n      statName\n    }\n    owgr\n  }\n}"
    }
    response = requests.post(url, headers=headers, json=data)

    return response.json()

def GetPlayerProfileCareer(playerId:str):
    data = {
        "operationName": "PlayerProfileCareer",
        "variables": {
            "playerId": "49303",
            "tourCode": "R"
        },
        "query": "query PlayerProfileCareer($playerId: String!, $tourCode: TourCode) {\n  playerProfileCareer(playerId: $playerId, tourCode: $tourCode) {\n    playerId\n    tourCode\n    events\n    wins\n    winsTitle\n    internationalWins\n    majorWins\n    cutsMade\n    runnerUp\n    second\n    third\n    top10\n    top25\n    years {\n      cutsMade\n      displaySeason\n      events\n      officialMoney\n      second\n      standingsPoints\n      standingsRank\n      third\n      top10\n      top25\n      tourCode\n      wins\n      withdrawn\n      year\n    }\n    officialMoney\n    tourPills {\n      tourCode\n      displayName\n    }\n    achievements {\n      title\n      value\n    }\n    tables {\n      tableName\n      tableDetail\n      rows {\n        rowTitle\n        rowTitleDetail\n        rowContent\n        secondContent\n      }\n    }\n    years {\n      tourCode\n      displaySeason\n      year\n      events\n      wins\n      second\n      third\n      top10\n      top25\n      cutsMade\n      withdrawn\n      officialMoney\n      standingsPoints\n      standingsRank\n    }\n  }\n}"
    }
    response = requests.post(url, headers=headers, json=data)

    return response.json()

def GetPlayerProfileSeasonResults(playerId:str):
    data = {
        "operationName": "PlayerProfileSeasonResults",
        "variables": {
            "playerId": "49303"
        },
        "query": "query PlayerProfileSeasonResults($playerId: ID!, $tourCode: TourCode, $year: Int) {\n  playerProfileSeasonResults(\n    playerId: $playerId\n    tourCode: $tourCode\n    year: $year\n  ) {\n    playerId\n    tour\n    displayYear\n    year\n    events\n    wins\n    top10\n    top25\n    cutsMade\n    missedCuts\n    withdrew\n    runnerUp\n    seasonPills {\n      tourCode\n      years {\n        year\n        displaySeason\n      }\n    }\n    cupRank\n    cupPoints\n    cupName\n    cupLogo\n    cupLogoDark\n    cupLogoAccessibilityText\n    rankLogo\n    rankLogoDark\n    rankLogoAccessibilityText\n    officialMoney\n    tournaments {\n      linkable\n      tournamentId\n      tournamentEndDate\n      tournamentName\n      finishPosition\n      r1\n      r2\n      r3\n      r4\n      r5\n      total\n      toPar\n      pointsRank\n      points\n      money\n      tourcastURL\n      tourcastURLWeb\n      linkable\n      fedexFallRank\n      fedexFallPoints\n      courseName\n      courseId\n    }\n    seasonRecap {\n      tourCode\n      displayMostRecentSeason\n      mostRecentRecapYear\n      items {\n        year\n        displaySeason\n        items {\n          tournamentId\n          year\n          title\n          body\n        }\n      }\n    }\n    amateurHighlights\n    tourcastEligible\n    secondaryCup {\n      cupRank\n      cupPoints\n      cupName\n      cupLogo\n      cupLogoDark\n      cupLogoAccessibilityText\n      rankLogo\n      rankLogoDark\n      rankLogoAccessibilityText\n    }\n  }\n}"
    }
    response = requests.post(url, headers=headers, json=data)

    return response.json()

def GetPlayerScorecardCompressed(playerId:str):
    data = {
        "operationName": "ScorecardCompressedV3",
        "variables": {
            "tournamentId": "R2024493",
            "playerId": "49303"
        },
        "query": "query ScorecardCompressedV3($tournamentId: ID!, $playerId: ID!) {\n  scorecardCompressedV3(tournamentId: $tournamentId, playerId: $playerId) {\n    id\n    payload\n  }\n}"
    }
    response = requests.post(url, headers=headers, json=data)

    return response.json()

def GetCourseStatDetails():
    data = {
        "operationName": "CourseStatsDetails",
        "variables": {
            "tourCode": "R",
            "queryType": "TOUGHEST_COURSE",
            "round": "ALL",
            "year": 2024
        },
        "query": "query CourseStatsDetails($tourCode: TourCode!, $queryType: CourseStatsId!, $round: ToughestRound, $year: Int) {\n  courseStatsDetails(\n    tourCode: $tourCode\n    queryType: $queryType\n    round: $round\n    year: $year\n  ) {\n    tourCode\n    year\n    round\n    displayYear\n    seasons {\n      year\n      displaySeason\n    }\n    headers\n    displayName\n    tableName\n    rows {\n      rank\n      displayName\n      values {\n        value\n        tendency\n      }\n      tournamentId\n      tournamentName\n    }\n    shareURL\n    roundPills {\n      display\n      queryVal\n    }\n  }\n}"
    }
    response = requests.post(url, headers=headers, json=data)

    return response.json()

def GetCourseStatOverview():
    data = {
        "operationName": "CourseStatsOverview",
        "variables": {
            "tourCode": "R",
            "year": 2024
        },
        "query": "query CourseStatsOverview($tourCode: TourCode!, $year: Int) {\n  courseStatsOverview(tourCode: $tourCode, year: $year) {\n    tourCode\n    year\n    categories {\n      header\n      detailId\n      items {\n        displayName\n        rank\n        image\n        details {\n          value\n          label\n        }\n      }\n    }\n  }\n}"
    }
    response = requests.post(url, headers=headers, json=data)

    return response.json()