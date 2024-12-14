import csv
import os.path
import requests
from pathlib import Path

from classes.StatCategory import StatCategory

from helpers.PathBuilder import *
from helpers.JSONDataMapping import *
from helpers.FileHelper import CreateDirectory, CleanName

# Call request for data and write file to data/<year>/...
def CallAndWriteStatData(category, subcategory, year: int, statId: int, filePath: str):    
    path = GetStatsPath(year=year, statsId= statId)
    x = requests.get(path)
    
    if (x.status_code != 200):
        pass
    else:
        yearDir = '/'.join(['data', year])
        categoryDir = '/'.join(['data', year, category])
        subcategoryDir = '/'.join(['data', year, category, subcategory])
        
        if os.path.isdir(yearDir) == False:
            CreateDirectory(year)
            
        if os.path.isdir(categoryDir) == False:
            CreateDirectory(categoryDir)
            
        if os.path.isdir(subcategoryDir) == False:
            CreateDirectory(subcategoryDir)
            
        with open(filePath, "wb") as file:
            file.write(x.content)
    
# Get all CSV stat detail files for a given year
def GetStatCsvs(year: int):
    categories = GetStatCategories()
    categories = [StatCategory(**c) for c in categories]

    stat_details = []
    current_year = str(year)
    
    # Dict
    stat_ids_dict = {}

    for c in categories:
        category = CleanName(c.category)
        
        for sc in c.subCategories:
            subCategory = CleanName(sc.displayName)

            for sd in sc.stats:
                obj = {}
                obj['category'] = c.category
                obj['subCategory'] = sc.displayName
                obj['statTitle'] = sd.statTitle
                obj['statId'] = sd.statId
                
                # If stat id is a duplicate
                if (sd.statId in stat_ids_dict):
                    obj['path'] = stat_ids_dict[sd.statId]
                    obj['duplicatedStatId'] = True
                else:
                    file_name = CleanName(sd.statTitle) + '.csv'
                    obj['path'] = '/'.join(['data', current_year, category, subCategory, file_name])
                    stat_ids_dict[sd.statId] = obj['path']
                    obj['duplicatedStatId'] = False

                stat_details.append(obj)
                
    # Mapping stat file data
    stat_detail_rows = []
    stat_detail_headers = ['Year', 'Index', 'Category', 'Subcategory', 'StatId', 'StatTitle', 'LocalPath']
    stat_detail_rows.append(stat_detail_headers)

    for (index, v) in enumerate(stat_details):
        print('Progress: {0}/{1}'.format(index, len(stat_details)), flush=True )

        statId = v['statId']
        category = v['category']
        subcategory = v['subCategory']
        path = v['path']
        statTitle = v['statTitle']

        row = [current_year, str(index), category, subcategory, statId, statTitle, path]
        stat_detail_rows.append(row)
        
        if (v['duplicatedStatId'] == False):
            current_file = Path(path)
            
            # if file does not exist currently, call it 
            if current_file.is_file(): continue
            else:
                try: CallAndWriteStatData(category, subCategory, year, statId, path)
                except Exception: continue
                        
    # Create file mapper file
    with open('data/' + current_year +'/file_map.csv', "w", newline='\n') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
        for row in stat_detail_rows:
            writer.writerow(row)
            
