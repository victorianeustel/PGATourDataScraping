import json
import os 

from classes.StatCategory import StatCategory

path = os.path.realpath(__file__) 
dir = os.path.dirname(path) 

dir = dir.replace('src', 'data') 
os.chdir(dir) 
print(dir) 

f = open('detail.json')
data = json.load(f)

categories = data['pageProps']['statDetails']['statCategories']
mapped_categories = [StatCategory(**c) for c in categories]
print(mapped_categories)