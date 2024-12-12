from DownloadStatsCsvs import GetStatCsvs
from helpers.FileHelper import DeleteEmptyDirectories, DeleteEmptyDataFiles
from classes.Year import Year
from classes.Player import Player
from helpers.JSONDataMapping import *
from helpers.CSVHelper import *
import os

# Get seasons / years that have data
# years = GetYears()
# mapped_years = [Year(**y) for y in years]

# # Trigger data ingestion call
# for year in mapped_years:
#     GetStatCsvs(year.year)
    
players = GetPlayers()
mapped_players = [Player(**p) for p in players]

for player in mapped_players:
    
    print(player.id + '-' + player.displayName)
    
# Clean up data files and directories
# path = os.getcwd() + '/data'
# DeleteEmptyDataFiles(path)
# DeleteEmptyDirectories(path)