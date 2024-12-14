from json_data_mapping import *
from players.player import *
from generate_csv_data import *
from pga_data_calls import *

def run_players_directory_task(players: list[Player]):
    with open('data/players/players_directory.csv', "w", newline='\n') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
        header = ['id', 'isActive', 'firstName', 'lastName', 'shortName', 'displayName', 'alphaSort', 'country', 'countryFlag', 'headshot', 'age', 'education', 'turnedPro']
        writer.writerow(header)
        for player in players:
            writer.writerow(player.ToArray())
        
