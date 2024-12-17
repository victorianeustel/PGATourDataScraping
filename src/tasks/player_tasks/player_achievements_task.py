from helpers.json_data_mapping import *
from helpers.pga_data_calls import *
from classes.players.player import *
from classes.players.player_profile_career import *
from helpers.csv_helper import *

def run_players_achievements_task(playerData: list[PlayerProfileCareer]):
    print(playerData)
    file_name = 'players_achievements.csv'
    players_path =  '/'.join(['data', 'players'])

    header = ['playerId', 'title', 'value']
    
    create_or_append_csv(players_path, file_name, "w", header = header )
    
    for player in playerData:
        create_or_append_csv(players_path, file_name, "a", content_rows= [a.ToArray() for a in player.achievements] )

