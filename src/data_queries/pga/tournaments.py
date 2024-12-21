from .api import PGA_API
import requests

def get_tournaments(tournamentIdsList: list[str]):
    data = {
        "operationName": "Tournaments",
        "variables": {
            "ids": tournamentIdsList
        },
        "query": "query Tournaments($ids: [ID!]) {\n  tournaments(ids: $ids) {\n    ...TournamentFragment\n  }\n}\n\nfragment TournamentFragment on Tournament {\n  id\n  tournamentName\n  tournamentLogo\n  tournamentLocation\n  tournamentStatus\n  roundStatusDisplay\n  roundDisplay\n  roundStatus\n  roundStatusColor\n  currentRound\n  timezone\n  pdfUrl\n  seasonYear\n  displayDate\n  country\n  state\n  city\n  scoredLevel\n  infoPath\n  events {\n    id\n    eventName\n    leaderboardId\n  }\n  courses {\n    id\n    courseName\n    courseCode\n    hostCourse\n    scoringLevel\n  }\n  weather {\n    logo\n    logoDark\n    logoAccessibility\n    tempF\n    tempC\n    condition\n    windDirection\n    windSpeedMPH\n    windSpeedKPH\n    precipitation\n    humidity\n  }\n  ticketsURL\n  tournamentSiteURL\n  formatType\n  features\n  conductedByLabel\n  conductedByLink\n  beautyImage\n  hideRolexClock\n  hideSov\n  headshotBaseUrl\n  rightRailConfig {\n    imageUrl\n    imageAltText\n    buttonLink\n    buttonText\n  }\n  shouldSubscribe\n  ticketsEnabled\n  useTournamentSiteURL\n  tournamentCategoryInfo {\n    type\n    logoLight\n    logoDark\n    label\n  }\n}"
    }
    response = requests.post(PGA_API.url, headers=PGA_API.headers, json=data)
    return response.json()
    
def get_tournaments_overview(tournamentId: str):
    data = {
        "operationName": "TournamentOverview",
        "variables": {
            "tournamentId": tournamentId
        },
        "query": "query TournamentOverview($tournamentId: ID!) {\n  tournamentOverview(tournamentId: $tournamentId) {\n    beautyImage\n    overview {\n      label\n      value\n      detail\n      secondaryDetail\n      wide\n      smallCopy\n    }\n    defendingChampion {\n      displaySeason\n      title\n      playerId\n      displayName\n      score\n      total\n      countryCode\n      seed\n      headshot\n    }\n    defendingTeamChampion {\n      displaySeason\n      title\n      playerId\n      displayName\n      score\n      total\n      countryCode\n      seed\n      headshot\n    }\n    pastChampions {\n      displaySeason\n      title\n      playerId\n      displayName\n      score\n      total\n      countryCode\n      seed\n      headshot\n    }\n    pastTeamChampions {\n      players {\n        displaySeason\n        title\n        playerId\n        displayName\n        score\n        total\n        countryCode\n        seed\n        headshot\n      }\n    }\n    ticketsURL\n    webviewBrowserControls\n    tourcastURL\n    tourcastURLWeb\n    shareURL\n    eventGuideURL\n    augmentedReality {\n      holes {\n        holeNumber\n      }\n    }\n    courses {\n      id\n      image\n      name\n      city\n      state\n      country\n      overview {\n        label\n        value\n        detail\n        secondaryDetail\n        wide\n        smallCopy\n      }\n    }\n    formatType\n    activation {\n      title\n      sponsorLogo\n      sponsorLogoDark\n      data\n      description\n      detail\n    }\n    tournamentCategoryInfo {\n      type\n      logoLight\n      logoDark\n      label\n    }\n  }\n}"
    }
    
    response = requests.post(PGA_API.url, headers=PGA_API.headers, json=data)
    return response.json()

def get_tournaments_past_results(tournamentId: str, year: str = None):
    data = {
        "operationName": "TournamentPastResults",
        "variables": {
            "tournamentPastResultsId": tournamentId,
            "year": year
        },
        "query": "query TournamentPastResults($tournamentPastResultsId: ID!, $year: Int) {\n  tournamentPastResults(id: $tournamentPastResultsId, year: $year) {\n    id\n    players {\n      id\n      position\n      player {\n        id\n        firstName\n        lastName\n        shortName\n        displayName\n        abbreviations\n        abbreviationsAccessibilityText\n        amateur\n        country\n        countryFlag\n        lineColor\n        seed\n        status\n        tourBound\n        assets {\n          ... on TourBoundAsset {\n            tourBoundLogo\n            tourBoundLogoDark\n          }\n        }\n      }\n      rounds {\n        score\n        parRelativeScore\n      }\n      additionalData\n      total\n      parRelativeScore\n    }\n    teams {\n      teamId\n      position\n      players {\n        id\n        firstName\n        lastName\n        shortName\n        displayName\n        abbreviations\n        abbreviationsAccessibilityText\n        amateur\n        country\n        countryFlag\n        lineColor\n        seed\n        status\n        tourBound\n        assets {\n          ... on TourBoundAsset {\n            tourBoundLogo\n            tourBoundLogoDark\n          }\n        }\n      }\n      additionalData\n      total\n      parRelativeScore\n      rounds {\n        score\n        parRelativeScore\n      }\n    }\n    rounds\n    additionalDataHeaders\n    availableSeasons {\n      year\n      displaySeason\n    }\n    winner {\n      id\n      firstName\n      lastName\n      totalStrokes\n      totalScore\n      countryFlag\n      countryName\n      purse\n      displayPoints\n      displayPurse\n      points\n      seed\n      pointsLabel\n      winnerIcon {\n        type\n        title\n        label\n        color\n      }\n    }\n    winningTeam {\n      id\n      firstName\n      lastName\n      totalStrokes\n      totalScore\n      countryFlag\n      countryName\n      purse\n      displayPoints\n      displayPurse\n      points\n      seed\n      pointsLabel\n      winnerIcon {\n        type\n        title\n        label\n        color\n      }\n    }\n    recap {\n      weather {\n        day\n        text\n      }\n      notes\n    }\n  }\n}"
    }
    
    response = requests.post(PGA_API.url, headers=PGA_API.headers, json=data)
    return response.json()

def get_upcoming_tournaments(tourCode: str = "R"):
    data = {
        "operationName": "UpcomingSchedule",
        "variables": {
            "tourCode": tourCode
        },
        "query": "query UpcomingSchedule($tourCode: String!, $year: String) {\n  upcomingSchedule(tourCode: $tourCode, year: $year) {\n    id\n    tournaments {\n      id\n      date\n      startDate\n      dateAccessibilityText\n      tournamentName\n      tournamentLogo\n      city\n      state\n      stateCode\n      country\n      countryCode\n      courseName\n      champion\n      championId\n      champions {\n        displayName\n        playerId\n      }\n      championEarnings\n      beautyImage\n      status {\n        roundStatusDisplay\n        roundDisplay\n        roundStatus\n        roundStatusColor\n      }\n      sortDate\n      sequenceNumber\n      purse\n      ticketsURL\n      tourStandingHeading\n      tourStandingValue\n      tournamentLogo\n      tournamentName\n      tournamentStatus\n      display\n      ticketsURL\n      sequenceNumber\n      tournamentSiteURL\n      useTournamentSiteURL\n    }\n  }\n}"
    }
    
    response = requests.post(PGA_API.url, headers=PGA_API.headers, json=data)
    return response.json()

def get_tournament_weather(tournamentId: str):
    data = {
        "operationName": "Weather",
        "variables": {
            "tournamentId": tournamentId
        },
        "query": "query Weather($tournamentId: ID!) {\n  weather(tournamentId: $tournamentId) {\n    title\n    sponsorLogo\n    accessibilityText\n    hourly {\n      title\n      condition\n      windDirection\n      windSpeedKPH\n      windSpeedMPH\n      humidity\n      precipitation\n      temperature {\n        ... on StandardWeatherTemp {\n          __typename\n          tempC\n          tempF\n        }\n        ... on RangeWeatherTemp {\n          __typename\n          minTempC\n          minTempF\n          maxTempC\n          maxTempF\n        }\n      }\n    }\n    daily {\n      title\n      condition\n      windDirection\n      windSpeedKPH\n      windSpeedMPH\n      humidity\n      precipitation\n      temperature {\n        ... on StandardWeatherTemp {\n          __typename\n          tempC\n          tempF\n        }\n        ... on RangeWeatherTemp {\n          __typename\n          minTempC\n          minTempF\n          maxTempC\n          maxTempF\n        }\n      }\n    }\n  }\n}"
    }
    
    response = requests.post(PGA_API.url, headers=PGA_API.headers, json=data)
    return response.json()

def get_tournament_recap(tournamentId: str):
    data = {
        "operationName": "TournamentRecap",
        "variables": {
            "tournamentId": "R2023003",
            "limit": 20
        },
        "query": "query TournamentRecap($tournamentId: String!, $limit: Int, $offset: Int) {\n  tournamentRecap(tournamentId: $tournamentId, limit: $limit, offset: $offset) {\n    tournamentId\n    durationDate\n    courses {\n      id\n      image\n      name\n      city\n      state\n      country\n      par\n      yardage\n    }\n    newsArticles {\n      id\n      headline\n      teaserHeadline\n      teaserContent\n      articleImage\n      url\n      shareURL\n      publishDate\n      updateDate\n      franchise\n      franchiseDisplayName\n      sponsor {\n        name\n        description\n        sponsorPrefix\n        logo\n        logoDark\n        image\n        websiteUrl\n        gam\n      }\n      brightcoveId\n      externalLinkOverride\n    }\n    videos {\n      ...VideoFragment\n    }\n  }\n}\n\nfragment VideoFragment on Video {\n  category\n  categoryDisplayName\n  created\n  description\n  descriptionNode {\n    ... on NewsArticleText {\n      __typename\n      value\n    }\n    ... on NewsArticleLink {\n      __typename\n      segments {\n        type\n        value\n        data\n        id\n        format {\n          variants\n        }\n        imageOrientation\n        imageDescription\n      }\n    }\n  }\n  duration\n  franchise\n  franchiseDisplayName\n  holeNumber\n  id\n  playerVideos {\n    firstName\n    id\n    lastName\n    shortName\n  }\n  poster\n  pubdate\n  roundNumber\n  shareUrl\n  shotNumber\n  startsAt\n  endsAt\n  thumbnail\n  title\n  tournamentId\n  tourCode\n  year\n  accountId\n  gamAccountId\n  videoAccountId\n  seqHoleNumber\n  sponsor {\n    name\n    description\n    logoPrefix\n    logo\n    logoDark\n    image\n    websiteUrl\n    gam\n  }\n  pinned\n  contentTournamentId\n}"
    }
    
    response = requests.post(PGA_API.url, headers=PGA_API.headers, json=data)
    return response.json()