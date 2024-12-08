import json
import os 

from classes.StatCategory import StatCategory

path = os.path.realpath(__file__) 
dir = os.path.dirname(path) 

dir = dir.replace('src', 'data/static') 
os.chdir(dir) 

f = open('detail.json')
data = json.load(f)

categories = data['pageProps']['statDetails']['statCategories']
mapped_categories = [StatCategory(**c) for c in categories]
for c in mapped_categories:
    print(str(c))
# print([str(c) for c in mapped_categories])