import json

# Loading instance of mapping json
def LoadJSON(filePath: str):
    f = open(filePath)
    return json.load(f)

# Get stat categories from mapping json
def GetStatCategories():
    data = LoadJSON('data/stats/detail.json')
    categories = data['pageProps']['statDetails']['statCategories']
    return categories

# Get years / seasons from mapping json
def GetYears():
    data = LoadJSON('data/stats/detail.json')
    years = data['pageProps']['statDetails']['yearPills']
    return years

def GetPlayers():
    data = LoadJSON('data/players/players-directory.json')

    players = data['data']['playerDirectory']['players']
    return players

def GetPlayerJsonData(playerId: str):
    data = LoadJSON('data/players/jsonData/' + playerId + '.json')
        
    return data

