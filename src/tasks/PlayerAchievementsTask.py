from helpers.JSONDataMapping import *
from helpers.PGADataCalls import *
from classes.Player import *
from classes.PlayerProfileCareer import *
from helpers.CSVHelper import *
from helpers.GenerateCSVData import * 

def RunPlayersAchievementsTask(playerData: list[PlayerProfileCareer]):
    print(playerData)
    file_name = 'players_achievements.csv'
    players_path =  '/'.join(['data', 'players'])

    header = ['playerId', 'title', 'value']
    
    CreateOrAppendCSV(players_path, file_name, "w", header = header )
    
    for player in playerData:
        
        CreateOrAppendCSV(players_path, file_name, "a", content_rows= [a.ToArray() for a in player.achievements] )

