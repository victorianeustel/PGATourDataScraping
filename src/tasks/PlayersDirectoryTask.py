from JSONDataMapping import *
from Player import *
from GenerateCSVData import *

players = GetPlayers()
mapped_players = [Player(**p) for p in players]

with open('data/players/players_directory.csv', "w", newline='\n') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
    header = ['id', 'isActive', 'firstName', 'lastName', 'shortName', 'displayName', 'alphaSort', 'country', 'countryFlag', 'headshot', 'age', 'education', 'turnedPro']
    writer.writerow(header)
    for player in mapped_players:
        writer.writerow(player.ToArray())