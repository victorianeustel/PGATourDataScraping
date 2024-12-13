from helpers.JSONDataMapping import *
from classes.Player import *
from helpers.GenerateCSVData import *
from helpers.PGADataCalls import *

players = GetPlayers()
mapped_players = [Player(**p) for p in players]

with open('data/players/players_directory.csv', "w", newline='\n') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
    header = ['id', 'isActive', 'firstName', 'lastName', 'shortName', 'displayName', 'alphaSort', 'country', 'countryFlag', 'headshot', 'age', 'education', 'turnedPro']
    writer.writerow(header)
    for player in mapped_players:
        writer.writerow(player.ToArray())
        
