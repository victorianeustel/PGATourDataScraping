from helpers.PathBuilder import *
import requests
import os
import json
from classes.StatCategory import StatCategory
from pathlib import Path

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
    
    filePath = '/'.join([current_year, filePath])
    
    path = get_stats_path(statsId= statId)
    x = requests.get(path)
    
    print(filePath)
    print(path)
    with open(filePath, "w") as file:
        file.writelines(x.text)
    

categories = GetStatCategories()

stat_details = []

def CleanName(name: str):
    cleaned_name = name \
        .replace('- ', '') \
        .replace(' ', '_') \
        .replace(',', '_') \
        .replace(':', '') \
        .replace('/', '') \
        .replace('*', '') \
        .replace('<', 'less-than') \
        .replace('>', 'greater-than') \
        .replace('|', 'or') \
        .replace('?', '') \
        .replace('\\', '') \
        .lower()

    return cleaned_name

current_year = '2024'
CreateDirectory(current_year)

for c in categories:
    category = CleanName(c.category)
    CreateDirectory('/'.join([current_year, category]))
    
    for sc in c.subCategories:
        subCategory = CleanName(sc.displayName)
        directory_name = '/'.join([current_year, category, subCategory])
        CreateDirectory(directory_name)

        for sd in sc.stats:
            file_name = CleanName(sd.statTitle) + '.csv'

            obj = {}
            obj['category'] = c.category
            obj['subCategory'] = sc.displayName
            obj['path'] = '/'.join([category, subCategory, file_name])
            obj['statTitle'] = sd.statTitle
            obj['statId'] = sd.statId
            
            stat_details.append(obj)

error_data = []

for index, v in enumerate(stat_details):
    statId = v['statId']
    category = v['category']
    subcategory = v['subCategory']
    path = v['path']
    summary = 'Index: {0} | Category: {1} | SubCategory: {2} | StatId: {3} | Path: {4}'.format(index,category, subCategory, statId, path)
    # print('Index: ' + index + '-' v['statsId'])
    # print(v['statId'])

    current_file = Path(path)
    # 
    # if current_file.is_file() == False:
    try:
        result = CallAndWriteStatData(statId, path)
    except Exception:
        error_data.append(v)
        print('ERROR: ' + summary)
        print(result)
        continue
        

    # stat_details.append(obj)