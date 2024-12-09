import csv
import pandas as pd

def IsEmptyCSV(path):
    df = pd.read_csv(path, sep=',', on_bad_lines='skip')
    row_count = len(df)


    # reader = csv.reader(path)
    # rows = GetCSVRowCount(reader)
    if df.empty:
        # print('-'.join([path, str(row_count)]))
        return True
    # if rows == 0 or rows == 1:
    #     return True
    else:
        return False
    
# def GetCSVRowCount(csvFile):
    
#     row_count = sum(1 for row in csvFile)  # fileObject is your csv.reader
#     return row_count