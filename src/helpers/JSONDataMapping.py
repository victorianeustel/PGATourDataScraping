import json

# Loading instance of mapping json
def LoadJSON():
    f = open('data/stats/detail.json')
    return json.load(f)
# Instance of json loaded
data = LoadJSON()

# Check if mapping json is loaded or not
def IsMappingJSONLoaded():
    if data:
        return True
    return False

# Get stat categories from mapping json
def GetStatCategories():
    if IsMappingJSONLoaded() == False:
        LoadJSON()

    categories = data['pageProps']['statDetails']['statCategories']
    return categories

# Get years / seasons from mapping json
def GetYears():
    if IsMappingJSONLoaded() == False:
        LoadJSON()
        
    years = data['pageProps']['statDetails']['yearPills']
    return years

def GetPlayers():
    f = open('data/players/players-directory.json')
    data = json.load(f)
        
    players = data['data']['playerDirectory']['players']
    return players
