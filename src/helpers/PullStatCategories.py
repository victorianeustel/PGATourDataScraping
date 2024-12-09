import json

def GetStatCategories():
    f = open('data/detail.json')
    data = json.load(f)

    categories = data['pageProps']['statDetails']['statCategories']
    
    return categories