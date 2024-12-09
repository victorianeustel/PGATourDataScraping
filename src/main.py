from DownloadStatsCsvs import GetStatCsvs
from Years import GetYears
from classes.Year import Year
from helpers.JSONDataMapping import *
from helpers.CSVHelper import *
import os

years = GetYears()
mapped_years = [Year(**y) for y in years]

# for year in mapped_years:
#     GetStatCsvs(year.year)
    
path = os.getcwd() + '/data'

print(path)

# result = IsEmptyCSV('/Users/victorianeustel/Documents/GitHub/PGATourDataScraping/data/2013/money_finishes/finishes/top_10_finishes.csv')
for subdir, dirs, files in os.walk(path):
    for file in files:
        if file.endswith(".csv"):
            fullPath = os.path.join(subdir, file)
            isEmpty = IsEmptyCSV(os.path.join(subdir, file))
            if isEmpty == True:
                os.remove(fullPath)

                # print(' '.join([subdir, file, str(isEmpty)]))
            # if isEmpty == True:
            #     print(os.path.join(subdir, file))

