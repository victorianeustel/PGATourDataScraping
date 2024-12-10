from DownloadStatsCsvs import GetStatCsvs
from helpers.FileHelper import DeleteEmptyDirectories, DeleteEmptyDataFiles
from Years import GetYears
from classes.Year import Year
from helpers.JSONDataMapping import *
from helpers.CSVHelper import *
import os

# Get seasons / years that have data
years = GetYears()
mapped_years = [Year(**y) for y in years]

# Trigger data ingestion call
for year in mapped_years:
    GetStatCsvs(year.year)
    
path = os.getcwd() + '/data'

# Clean up data files and directories
DeleteEmptyDataFiles(path)
DeleteEmptyDirectories(path)