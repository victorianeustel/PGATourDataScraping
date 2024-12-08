from helpers.PathBuilder import *
import requests
import os
import json
from classes.StatCategory import StatCategory

def CreateDirectory(directory_name):
    try:
        os.mkdir(directory_name)
        print(f"Directory '{directory_name}' created successfully.")
    except FileExistsError:
        print(f"Directory '{directory_name}' already exists.")
    except PermissionError:
        print(f"Permission denied: Unable to create '{directory_name}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

def GetStatCategories():
    path = os.path.realpath(__file__) 
    dir = os.path.dirname(path) 

    dir = dir.replace('src', 'data') 
    os.chdir(dir) 

    f = open('detail.json')
    data = json.load(f)

    categories = data['pageProps']['statDetails']['statCategories']
    mapped_categories = [StatCategory(**c) for c in categories]

    return mapped_categories

def CallAndWriteStatData(statId: int, filePath: str):
    # cwd = os.getcwd()  # Get the current working directory (cwd)
    # files = os.listdir(cwd)  # Get all the files in that directory
    # print("Files in %r: %s" % (cwd, files))
    
    filePath = filePath
    
    path = get_stats_path(statsId= statId)
    x = requests.get(path)
    
    print(filePath)
    print(path)
    with open(filePath, "w") as file:
        file.writelines(x.text)
    

categories = GetStatCategories()

stat_details = []

def CleanName(statTitle: str):
    cleaned_name = statTitle \
        .replace('- ', '') \
        .replace(' ', '_') \
        .replace(':', '')
    return cleaned_name

for c in categories:
    category = c.category
    CreateDirectory(category.lower())
    for sc in c.subCategories:
        subCategory = sc.displayName
        cleaned_subCategory = CleanName(subCategory)
        directory_name = '/'.join([category.lower(), cleaned_subCategory.lower()])
        CreateDirectory(directory_name)

        for sd in sc.stats:
            obj = {}
            obj['category'] = category
            obj['subCategory'] = subCategory
            file_name = CleanName(sd.statTitle) + '.csv'
            obj['path'] = '/'.join([category.lower(), cleaned_subCategory.lower(), file_name])
            obj['statTitle'] = sd.statTitle
            obj['statId'] = sd.statId
            
            stat_details.append(obj)
            
for v in stat_details:
    print(v['statId'])
    statId = v['statId']
    path = v['path']
    try:
        CallAndWriteStatData(statId, path)
    except:
        continue
    # stat_details.append(obj)