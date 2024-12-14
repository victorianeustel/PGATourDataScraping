from helpers.JSONDataMapping import *
from helpers.PGADataCalls import *
from classes.Player import *
from classes.PlayerProfileCareer import *
from helpers.CSVHelper import *
from helpers.GenerateCSVData import * 

def RunPlayerYearsTask(playerData: list[PlayerProfileCareer]):
    print(playerData)
    file_name = 'players_years.csv'
    players_path =  '/'.join(['data', 'players'])

    header = ['playerId', 'year', 'cutsMade', 'displaySeason',
              'events','officialMoney', 'second','standingsPoints',
              'standingsRank','third','top10','top25','tourCode', 'wins', 'withdrawn']
    
    CreateOrAppendCSV(players_path, file_name, "w", header = header )
    
    for player in playerData:
        
        CreateOrAppendCSV(players_path, file_name, "a", content_rows= [y.ToArray() for y in player.years] )

