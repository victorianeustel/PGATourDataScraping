from helpers.dataframe_comparer import *
from data.pga.stats import *

import csv
import pandas as pd
import json
import requests
import io

stat_years = []

with open('data/stats/stat_years.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    reader.__next__()
    for row in reader:
        stat_years.append(int(row[0]))
        
df = pd.read_csv('data/stats/stat_categories.csv', sep=',', on_bad_lines='skip', dtype = str)
stat_data = df[['stat_id', 'file_name']].groupby('stat_id', axis=0).first()
# stat_ids = df['stat_id'].unique()

unique_stat_ct = len(stat_data)
print(unique_stat_ct)
stats_file_dict = {}

# each year
for y in stat_years[0:1]:
    for i, file_name in stat_data.itertuples():    # print(f"Row {i}: {df.loc[i]}")
        df_row = stat_data.loc[i]
        row_num = df_row.name
        stat_id = i
        writing_type = "w"
        if stat_id in stats_file_dict:
            writing_type = "a"
        else:
            stats_file_dict[stat_id] = file_name
        
        filePath = "data/stats/stat_details/" + file_name

        writing_type = writing_type 
        
        path = get_stats_path(year=y, statsId= stat_id)
        response = requests.get(path)
        resp_content = str(response.content).split('\\n')

        with open(filePath, writing_type) as file:
            writer = csv.writer(file, delimiter= ',')
            
            reader = csv.reader(resp_content, delimiter=',')
            
            # print(next(reader))
            
            csv_rows = []
            
            if (writing_type == "w"):
                header = next(reader)
                header.append('YEAR')
                csv_rows.append(header)
                
            for row in reader:
                row.append(y)
                csv_rows.append(row)
                
            writer.writerows(csv_rows)

            
