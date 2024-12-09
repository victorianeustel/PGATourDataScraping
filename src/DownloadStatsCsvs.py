from helpers.PathBuilder import *
import requests
from classes.StatCategory import StatCategory
from helpers.JSONDataMapping import *
from pathlib import Path
import csv
from helpers.FileHelper import CreateDirectory, CleanName

def CallAndWriteStatData(statId: int, filePath: str):    
    path = get_stats_path(statsId= statId)
    x = requests.get(path)
    
    with open(filePath, "wb") as file:
        file.write(x.content)
    
def GetStatCsvs(current_year: str):
    categories = GetStatCategories()
    categories = [StatCategory(**c) for c in categories]

    stat_details = []

    CreateDirectory('data/' + current_year)
    stat_ids_dict = {}

    for c in categories:
        category = CleanName(c.category)
        CreateDirectory('/'.join(['data', current_year, category]))
        
        for sc in c.subCategories:
            subCategory = CleanName(sc.displayName)
            directory_name = '/'.join(['data', current_year, category, subCategory])
            CreateDirectory(directory_name)

            for sd in sc.stats:
                obj = {}
                obj['category'] = c.category
                obj['subCategory'] = sc.displayName
                obj['statTitle'] = sd.statTitle
                obj['statId'] = sd.statId
                
                isDuplicate = sd.statId in stat_ids_dict                
                if sd.statId in stat_ids_dict:
                    obj['path'] = stat_ids_dict[sd.statId]
                    obj['duplicatedStatId'] = True
                else:
                    file_name = CleanName(sd.statTitle) + '.csv'
                    obj['path'] = '/'.join(['data', current_year, category, subCategory, file_name])
                    stat_ids_dict[sd.statId] = obj['path']
                    obj['duplicatedStatId'] = False

                stat_details.append(obj)

    error_data = []

    stat_detail_rows = []
    stat_detail_headers = ['Year', 'Index', 'Category', 'Subcategory', 'StatId', 'StatTitle', 'LocalPath']
    stat_detail_rows.append(stat_detail_headers)

    for index, v in enumerate(stat_details):
        print('Progress: {0}/{1}'.format(index, len(stat_details)), flush=True )

        statId = v['statId']
        category = v['category']
        subcategory = v['subCategory']
        path = v['path']
        statTitle = v['statTitle']
        summary = 'Index: {0} | Category: {1} | SubCategory: {2} | StatId: {3} | Path: {4}'.format(index,category, subCategory, statId, path)

        row = [current_year, str(index), category, subcategory, statId, statTitle, path]
        stat_detail_rows.append(row)
        
        if v['duplicatedStatId'] == False:
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
                        
    # Create file mapper file
    with open('data/' + current_year +'/file_map.csv', "w", newline='\n') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
        for row in stat_detail_rows:
            writer.writerow(row)

    # Print errors
    if error_data:
        print('---------ERRORS---------')
        for error in error_data:
            summary = 'Category: {1} | SubCategory: {2} | StatId: {3} | Path: {4}'.format(category, subCategory, statId, path)
            print(summary)