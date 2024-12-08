from helpers.PathBuilder import *
import requests
import os
import json
from classes.StatCategory import StatCategory
from pathlib import Path
import csv

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
    path = get_stats_path(statsId= statId)
    x = requests.get(path)
    
    with open(filePath, "wb") as file:
        file.write(x.content)
    
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
            obj['path'] = '/'.join([current_year, category, subCategory, file_name])
            obj['statTitle'] = sd.statTitle
            obj['statId'] = sd.statId
            
            stat_details.append(obj)

error_data = []

stat_detail_rows = []
stat_detail_headers = ['Year', 'Index', 'Category', 'Subcategory', 'StatId', 'StatTitle', 'LocalPath']
stat_detail_rows.append(stat_detail_headers)

for index, v in enumerate(stat_details):
    statId = v['statId']
    category = v['category']
    subcategory = v['subCategory']
    path = v['path']
    statTitle = v['statTitle']
    summary = 'Index: {0} | Category: {1} | SubCategory: {2} | StatId: {3} | Path: {4}'.format(index,category, subCategory, statId, path)

    row = [current_year, str(index), category, subcategory, statId, statTitle, path]
    stat_detail_rows.append(row)
    
    current_file = Path(path)
    
    # if file does not exist currently, call it 
    if current_file.is_file():
        continue
    else:
        try:
            CallAndWriteStatData(statId, path)
        except Exception:
            error_data.append(v)
            print('ERROR: ' + summary)
            continue

with open('file_map.csv', "w", newline='\n') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
    for row in stat_detail_rows:
        writer.writerow(row)

print('---------ERRORS---------')
for error in error_data:
    summary = 'Category: {1} | SubCategory: {2} | StatId: {3} | Path: {4}'.format(category, subCategory, statId, path)
    print(summary)