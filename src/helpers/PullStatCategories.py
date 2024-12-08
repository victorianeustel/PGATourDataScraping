import json
import os 

# from classes.StatCategory import StatCategory

def GetStatCategories():
    path = os.path.realpath(__file__) 
    dir = os.path.dirname(path) 

    dir = dir.replace('src', 'data') 
    os.chdir(dir) 

    f = open('detail.json')
    data = json.load(f)

    categories = data['pageProps']['statDetails']['statCategories']
    
    return categories

    # for c in mapped_categories:
    #     print(str(c))
# print([str(c) for c in mapped_categories])