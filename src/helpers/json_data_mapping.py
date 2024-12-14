import json

# Loading instance of mapping json
def load_json(filePath: str):
    f = open(filePath)
    return json.load(f)

# Get stat categories from mapping json
def get_stat_categories():
    data = load_json('data/stats/detail.json')
    categories = data['pageProps']['statDetails']['statCategories']
    return categories

# Get years / seasons from mapping json
def get_years():
    data = load_json('data/stats/detail.json')
    years = data['pageProps']['statDetails']['yearPills']
    return years

def get_players():
    data = load_json('data/players/players-directory.json')

    players = data['data']['playerDirectory']['players']
    return players

def get_players_json_data(playerId: str):
    data = load_json('data/players/jsonData/' + playerId + '.json')
        
    return data

