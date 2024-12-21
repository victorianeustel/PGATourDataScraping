from helpers.dataframe_comparer import *

import pandas as pd
import json

df = pd.read_csv('data/stats/stat_categories.csv', sep=',', on_bad_lines='skip')
unique_categories = df['category'].unique()
print(unique_categories)
dict = {}

matched_tables={}

for uc in unique_categories:
    dict[uc] = {}
    print(uc)
    cat_df = df[df['category'] == uc]
    sc_cat = cat_df['subcategory_name'].unique()
    print(sc_cat)
    for sc in sc_cat:
        temp = cat_df[cat_df['subcategory_name'] == sc]
        cat_files = temp['file_name'].unique()
        dict[uc][sc] = cat_files 
        
for cindex, uc in enumerate(unique_categories):
    sc_df = df[df['category'] == uc]
    subcats = sc_df['subcategory_name'].unique()
    for sc in subcats:
        try:
            files = dict[uc][sc]
            matched_tables[uc] = {}
            base_columns = pd.read_csv('data/combined_stats/' + files[0], sep=',').columns
            base_cols_str = ','.join(base_columns)
            match = []
            unmatched = []
            for index, f in enumerate(files[1: len(files)]):
                print('category: {0} / {1} subcategory {2} / {3}'.format(cindex, len(unique_categories), index + 1, len(files)))

                try:
                    next_columns = pd.read_csv('data/combined_stats/' +f, sep=',').columns
                    if (len(base_columns) == len(next_columns)):
                        match.append(f)
                    else:
                        unmatched.append(f)
                except:
                    continue
                
            if len(match) > 0 or len(unmatched) > 0:
                matched_tables[uc][sc] = { "base": base_cols_str,
                                "matched": match, 
                                "unmatched": unmatched}
        except:
            continue
with open('data/matched_tables.json', 'w') as k:
    json.dump(matched_tables, k)