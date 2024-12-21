from .api import PGA_API
import requests

def get_tour_cup_split():
    data = {
        "operationName": "TourCupSplit",
        "variables": {
            "tourCode": "R",
            "id": "fedex",
            "year": 2024
        },
        "query": "query TourCupSplit($tourCode: TourCode!, $id: String, $year: Int, $eventQuery: StatDetailEventQuery) {\n  tourCupSplit(tourCode: $tourCode, id: $id, year: $year, eventQuery: $eventQuery) {\n    ...TourCupSplitMeta\n    fixedHeaders\n    columnHeaders\n    rankingsHeader\n    rankEyebrow\n    pointsEyebrow\n    message\n    partner\n    partnerLink\n    projectedPlayers {\n      ...Player\n      ...InfoRow\n    }\n    officialPlayers {\n      ...Player\n      ...InfoRow\n    }\n    yearPills {\n      year\n      displaySeason\n    }\n    winner {\n      id\n      rank\n      firstName\n      lastName\n      displayName\n      shortName\n      countryFlag\n      country\n      earnings\n      totals {\n        label\n        value\n      }\n    }\n  }\n}\n\nfragment TourCupSplitMeta on TourCupSplit {\n  id\n  title\n  detailCopy\n  projectedTitle\n  projectedLive\n  season\n  description\n  logo\n  options\n  tournamentPills {\n    tournamentId\n    displayName\n  }\n}\n\nfragment Player on TourCupCombinedPlayer {\n  __typename\n  id\n  firstName\n  lastName\n  displayName\n  shortName\n  countryFlag\n  country\n  rankingData {\n    projected\n    official\n    event\n    movement\n    movementAmount\n    logo\n    logoDark\n  }\n  pointData {\n    projected\n    official\n    event\n    movement\n    movementAmount\n    logo\n    logoDark\n  }\n  projectedSort\n  officialSort\n  thisWeekRank\n  previousWeekRank\n  columnData\n  tourBound\n}\n\nfragment InfoRow on TourCupCombinedInfo {\n  logo\n  logoDark\n  text\n  sortValue\n  toolTip\n}"
    }
    response = requests.post(PGA_API.url, headers=PGA_API.headers, json=data)
    return response.json()