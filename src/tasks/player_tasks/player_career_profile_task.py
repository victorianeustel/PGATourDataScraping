from helpers.csv_helper import *

from data_queries.pga.players import *

from classes.players.player import *
from classes.players.player_profile_career import *

from .player_years_task import *
from .player_achievements_task import *

def run_player_career_profiles_task(
    players: list[Player],
    save_career_profiles:bool = True, 
    save_players_years:bool = True, 
    save_players_achievements:bool = True):
    if (save_career_profiles):
        career_profiles_path =  '/'.join(['data', 'players'])

        header = ['playerId', 'tourCode', 'events', 'wins','winsTitle','internationalWins',
                'majorWins','cutsMade','runnerUp','second','third','top10','top25','officialMoney']
        
        create_or_append_csv(career_profiles_path, 'career_profiles.csv', "w", header = header )

    player_career_data = []

    for (index, player) in enumerate(players):
        print('Progress: {0}/{1}'.format(index, len(players)), flush=True )

        playerId = player.id
        playerData = get_player_profile_career(playerId)
            
        player_career_data_obj = PlayerProfileCareer(**playerData['data']['playerProfileCareer'])

        player_career_data.append(player_career_data_obj)

        if (save_career_profiles): 
            create_or_append_csv(career_profiles_path, 'career_profiles.csv', "a", content_rows=[player_career_data_obj.ToArray()]) 
            
    if (save_players_years):run_player_years_task(player_career_data)
    if (save_players_achievements): run_players_achievements_task(player_career_data)