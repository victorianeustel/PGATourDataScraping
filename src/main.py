from DownloadStatsCsvs import *
from helpers.FileHelper import *
from classes.Year import Year
from classes.Player import Player
from classes.PlayerProfileCareer import PlayerProfileCareer
from helpers.JSONDataMapping import *
from helpers.CSVHelper import *
from GetPlayersData import *
import os
from GenerateCSVData import *
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

# for player in mapped_players:
#     playerId = player.id
#     playerData = GetPlayerData(playerId)
#     json_object = json.dumps(playerData, indent=4)

#     with open('data/players/jsonData/' + player.id +'.json', "w") as file:
#          file.write(json_object)

playerCareerDataPath = os.getcwd() + '/data/players/jsonData'
playersCareerData = GetAllFilesInDirectory(playerCareerDataPath)

player_career_data_json = [LoadJSON(p) for p in playersCareerData]
player_career_data = [PlayerProfileCareer(**p['data']['playerProfileCareer']) for p in player_career_data_json]

career_profiles_path =  '/'.join(['data', 'players'])
# CreateDirectory(career_profiles_path)

player_career_profile_header = player_career_data[0].GetListOfPropertyNames()
player_career_csv_rows = [p.ToArray() for p in player_career_data]

CreateCSV(career_profiles_path, 'career_profiles.csv', "w", player_career_profile_header, player_career_csv_rows)

# # Clean up data files and directories
# path = os.getcwd() + '/data'
# DeleteEmptyDataFiles(path)
# DeleteEmptyDirectories(path)