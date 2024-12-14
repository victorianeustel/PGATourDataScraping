from helpers.JSONDataMapping import *
from helpers.PGADataCalls import *
from classes.Player import *
from classes.PlayerProfileCareer import *
from helpers.CSVHelper import *
from helpers.CSVHelper import *
from .PlayerYearsTask import *
from .PlayerAchievementsTask import *

def RunGetPlayerCareerProfilesTask(
    players: list[Player],
    save_career_profiles:bool = True, 
    save_players_years:bool = True, 
    save_players_achievements:bool = True):
    if (save_career_profiles):
        career_profiles_path =  '/'.join(['data', 'players'])

        header = ['playerId', 'tourCode', 'events', 'wins','winsTitle','internationalWins',
                'majorWins','cutsMade','runnerUp','second','third','top10','top25','officialMoney']
        
        CreateOrAppendCSV(career_profiles_path, 'career_profiles.csv', "w", header = header )

    player_career_data = []

    for (index, player) in enumerate(players):
        print('Progress: {0}/{1}'.format(index, len(players)), flush=True )

        playerId = player.id
        playerData = GetPlayerData(playerId)
            
        player_career_data_obj = PlayerProfileCareer(**playerData['data']['playerProfileCareer'])

        player_career_data.append(player_career_data_obj)

        if (save_career_profiles): 
            CreateOrAppendCSV(career_profiles_path, 'career_profiles.csv', "a", content_rows=[player_career_data_obj.ToArray()]) 
            
    if (save_players_years):RunPlayerYearsTask(player_career_data)
    if (save_players_achievements): RunPlayersAchievementsTask(player_career_data)