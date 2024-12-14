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

