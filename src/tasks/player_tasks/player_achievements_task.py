from json_data_mapping import *
from pga_data_calls import *
from players.player import *
from players.player_profile_career import *
from csv_helper import *
from generate_csv_data import * 

def run_players_achievements_task(playerData: list[PlayerProfileCareer]):
    print(playerData)
    file_name = 'players_achievements.csv'
    players_path =  '/'.join(['data', 'players'])

    header = ['playerId', 'title', 'value']
    
    create_or_append_csv(players_path, file_name, "w", header = header )
    
    for player in playerData:
        create_or_append_csv(players_path, file_name, "a", content_rows= [a.ToArray() for a in player.achievements] )
