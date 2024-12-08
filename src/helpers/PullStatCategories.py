import json
import os 

def GetStatCategories():
    path = os.path.realpath(__file__) 
    dir = os.path.dirname(path) 

    dir = dir.replace('src', 'data') 
    os.chdir(dir) 

    f = open('detail.json')
    data = json.load(f)

    categories = data['pageProps']['statDetails']['statCategories']
    
    return categories