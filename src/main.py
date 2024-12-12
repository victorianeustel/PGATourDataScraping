from tasks.PlayerStatsTask import *
from helpers.FileHelper import *
from classes.Year import Year
from classes.Player import Player
from classes.PlayerProfileCareer import PlayerProfileCareer
from helpers.JSONDataMapping import *
from helpers.CSVHelper import *
from PGADataCalls import *
import os
from helpers.GenerateCSVData import *

# Get seasons / years that have data
years = GetYears()
mapped_years = [Year(**y) for y in years]

# # Trigger data ingestion call
for year in mapped_years:
    GetStatCsvs(year.year)
    
# Clean up data files and directories
path = os.getcwd() + '/data'
DeleteEmptyDataFiles(path)
DeleteEmptyDirectories(path)