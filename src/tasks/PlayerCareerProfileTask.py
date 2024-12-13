import json
from helpers.JSONDataMapping import *
from helpers.PGADataCalls import *
from classes.Player import *
from classes.PlayerProfileCareer import *
from helpers.CSVHelper import *
from helpers.GenerateCSVData import *

def RunGetPlayerCareerProfilesTask():
    career_profiles_path =  '/'.join(['data', 'players'])

    header = ['playerId', 'tourCode', 'events', 'wins','winsTitle','internationalWins',
            'majorWins','cutsMade','runnerUp','second','third','top10','top25','officialMoney']
    
    CreateOrAppendCSV(career_profiles_path, 'career_profiles2.csv', "w", header = header )
    
    players = GetPlayers()
    mapped_players = [Player(**p) for p in players]

    player_career_data = []

    for index, player in enumerate(mapped_players):
        print('Progress: {0}/{1}'.format(index, len(mapped_players)), flush=True )

        print()
        playerId = player.id
        playerData = GetPlayerData(playerId)
            
        # player_career_data_json = LoadJSON(playerData)
        player_career_data_obj = PlayerProfileCareer(**playerData['data']['playerProfileCareer'])

        player_career_data.append([player_career_data_obj])


        CreateOrAppendCSV(career_profiles_path, 'career_profiles2.csv', "a", content_rows=[player_career_data_obj.ToArray()]) 

    # player_career_csv_rows = [p.ToArray() for p in player_career_data]

    # player_career_profile_header = player_career_data[0].GetListOfPropertyNames()

