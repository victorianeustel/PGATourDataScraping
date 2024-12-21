from helpers.dataframe_comparer import *
from helpers.csv_helper import *

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
# print(unique_stat_ct)
stats_file_dict = {}

# each year
for index, y in enumerate(stat_years):
    stat_index = 1
    for stat_id, file_name in stat_data.itertuples(): 
    # for stat_id, file_name in {"02675": "sg_total.csv"}.items():
        stat_index = stat_index + 1
        df_row = stat_data.loc[stat_id]
        print("YEAR {0} ({1} / {2}) - STAT {3} {4} / {5}"
            .format(y, 
                    index, 
                    len(stat_years), 
                    stat_id,
                    stat_index,
                    unique_stat_ct 
                    ), 
            end='\r'
            )

        writing_type = "w"
        if stat_id in stats_file_dict:
            writing_type = "a"
        else:
            stats_file_dict[stat_id] = file_name
        
        filePath = "data/stats/stat_details/" + file_name
        
        path = get_stats_path(year=y, statsId= stat_id)
        response = requests.get(path, stream=True)
        response_bytes = response.content.decode('utf-8')
        header = pd.read_csv(io.StringIO(response_bytes), index_col=0, nrows=0).columns.tolist()
        # print(header)
        # col_count = len(header)

        df = pd.read_csv(io.StringIO(response_bytes), usecols=header)
        df['YEAR'] = y
        move_column_inplace(df, 'YEAR', 0)
        cols = df.columns.tolist()
        
        if df.empty:
            continue
        if (writing_type == "w"):
            df.to_csv(filePath, index=False)
        elif (writing_type == "a"):
            base_df = pd.read_csv(filePath)
            if (len(base_df.columns.tolist()) != len(cols)):
                continue
            
            temp = pd.concat([base_df, df])
            temp.to_csv(filePath, index = False)