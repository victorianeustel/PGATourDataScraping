from dotenv import load_dotenv

from classes.Year import Year
from classes.Player import Player
from classes.PlayerProfileCareer import *
from classes.Schedule import *

from helpers.FileHelper import *
from helpers.JSONDataMapping import *
from helpers.CSVHelper import *
from helpers.PGADataCalls import *

from tasks.PlayerCareerProfileTask import *
from tasks.PlayersDirectoryTask import *
from tasks.PlayerStatsTask import *
from tasks.ScheduleTasks import *

load_dotenv()
SetAPIKey(os.environ.get('PGA_TOUR_API_KEY'))

# Get seasons / years that have data
years = GetYears()
mapped_years = [Year(**y) for y in years]

# Trigger data ingestion call
for year in mapped_years:
    GetStatCsvs(year.year)

players = GetPlayers()
mapped_players = [Player(**p) for p in players]

# Run Tasks
RunGetScheduleTasks()
RunGetPlayersDirectoryTask()
RunGetPlayerCareerProfilesTask(
    players = mapped_players, 
    save_career_profiles = False, 
    save_players_achievements = False, 
    save_players_years = False)
    
# Clean up data files and directories
path = os.getcwd() + '/data'
DeleteEmptyDataFiles(path)
DeleteEmptyDirectories(path)

