from DownloadStatsCsvs import GetStatCsvs
from helpers.FileHelper import DeleteEmptyDirectories, DeleteEmptyDataFiles
from classes.Year import Year
from classes.Player import Player
from helpers.JSONDataMapping import *
from helpers.CSVHelper import *
from GetPlayersData import *
import os
import csv

# Get seasons / years that have data
# years = GetYears()
# mapped_years = [Year(**y) for y in years]

# # # Trigger data ingestion call
# for year in mapped_years:
#     GetStatCsvs(year.year)
    
players = GetPlayers()
mapped_players = [Player(**p) for p in players]

# with open('data/players/players_directory.csv', "w", newline='\n') as csvfile:
#     writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
#     header = ['id', 'isActive', 'firstName', 'lastName', 'shortName', 'displayName', 'alphaSort', 'country', 'countryFlag', 'headshot', 'age', 'education', 'turnedPro']
#     writer.writerow(header)
#     for player in mapped_players:
#         writer.writerow(player.ToArray())

for player in mapped_players:
    playerId = player.id
    playerData = GetPlayerData(playerId)
    json_object = json.dumps(playerData, indent=4)

    with open('data/players/jsonData/' + player.id +'.json', "w") as file:
         file.write(json_object)

    
# # Clean up data files and directories
# path = os.getcwd() + '/data'
# DeleteEmptyDataFiles(path)
# DeleteEmptyDirectories(path)