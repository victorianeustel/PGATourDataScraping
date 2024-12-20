from helpers.dataframe_comparer import *

import pandas as pd


df = pd.read_csv('data/stats/stat_categories.csv', sep=',', on_bad_lines='skip')
