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

for subdir, dirs, files in os.walk(path):
    for file in files:
        if file.endswith(".csv"):
            fullPath = os.path.join(subdir, file)
            isEmpty = IsEmptyCSV(os.path.join(subdir, file))
            if isEmpty == True:
                os.remove(fullPath)

def delete_empty_folders(root):

    deleted = set()
    
    for current_dir, subdirs, files in os.walk(root, topdown=False):

        still_has_subdirs = False
        for subdir in subdirs:
            if os.path.join(current_dir, subdir) not in deleted:
                still_has_subdirs = True
                break
    
        if not any(files) and not still_has_subdirs:
            os.rmdir(current_dir)
            deleted.add(current_dir)

    return deleted

delete_empty_folders(path)