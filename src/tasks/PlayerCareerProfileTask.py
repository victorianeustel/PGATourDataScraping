from helpers.JSONDataMapping import *
from helpers.PGADataCalls import *
from classes.Player import *
from classes.PlayerProfileCareer import *
from helpers.CSVHelper import *
from helpers.GenerateCSVData import *
from .PlayerYearsTask import *
from .PlayerAchievementsTask import *

def RunGetPlayerCareerProfilesTask():
    career_profiles_path =  '/'.join(['data', 'players'])

    header = ['playerId', 'tourCode', 'events', 'wins','winsTitle','internationalWins',
            'majorWins','cutsMade','runnerUp','second','third','top10','top25','officialMoney']
    
    # CreateOrAppendCSV(career_profiles_path, 'career_profiles.csv', "w", header = header )
    
    players = GetPlayers()
    mapped_players = [Player(**p) for p in players]

    player_career_data = []

    for index, player in enumerate(mapped_players):
        print('Progress: {0}/{1}'.format(index, len(mapped_players)), flush=True )

        playerId = player.id
        playerData = GetPlayerData(playerId)
            
        player_career_data_obj = PlayerProfileCareer(**playerData['data']['playerProfileCareer'])

        player_career_data.append(player_career_data_obj)

        # CreateOrAppendCSV(career_profiles_path, 'career_profiles.csv', "a", content_rows=[player_career_data_obj.ToArray()]) 
    RunPlayerYearsTask(player_career_data)
    RunPlayersAchievementsTask(player_career_data)