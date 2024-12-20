from classes.players.player import *
from classes.players.player_profile_career import *

from helpers.csv_helper import *

def run_player_years_task(playerData: list[PlayerProfileCareer]):
    file_name = 'players_years.csv'
    players_path =  '/'.join(['data', 'players'])

    header = ['playerId', 'year', 'cutsMade', 'displaySeason',
            'events','officialMoney', 'second','standingsPoints',
            'standingsRank','third','top10','top25','tourCode', 'wins', 'withdrawn']
    
    create_or_append_csv(players_path, file_name, "w", header = header )
    
    for player in playerData:
        
        create_or_append_csv(players_path, file_name, "a", content_rows= [y.ToArray() for y in player.years] )

