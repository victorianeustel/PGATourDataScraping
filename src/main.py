from tasks.DownloadStatsCsvs import *
from helpers.FileHelper import *
from classes.Year import Year
from classes.Player import Player
from classes.PlayerProfileCareer import PlayerProfileCareer
from helpers.JSONDataMapping import *
from helpers.CSVHelper import *
from tasks.GetPlayersData import *
import os
from helpers.GenerateCSVData import *
import csv

# Get seasons / years that have data
years = GetYears()
mapped_years = [Year(**y) for y in years]

# # Trigger data ingestion call
for year in mapped_years:
    GetStatCsvs(year.year)
    
players = GetPlayers()
mapped_players = [Player(**p) for p in players]

with open('data/players/players_directory.csv', "w", newline='\n') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
    header = ['id', 'isActive', 'firstName', 'lastName', 'shortName', 'displayName', 'alphaSort', 'country', 'countryFlag', 'headshot', 'age', 'education', 'turnedPro']
    writer.writerow(header)
    for player in mapped_players:
        writer.writerow(player.ToArray())


# # Clean up data files and directories
path = os.getcwd() + '/data'
DeleteEmptyDataFiles(path)
DeleteEmptyDirectories(path)