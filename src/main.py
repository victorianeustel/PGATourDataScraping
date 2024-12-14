from dotenv import load_dotenv

from classes.Year import Year
from classes.Player import Player
from classes.PlayerProfileCareer import *
from classes.Schedule import *

from helpers.FileHelper import *
from helpers.JSONDataMapping import *
from helpers.CSVHelper import *
from helpers.PGADataCalls import *
from helpers.GenerateCSVData import *

from tasks.PlayerCareerProfileTask import *
from tasks.PlayersDirectoryTask import *
from tasks.PlayerStatsTask import *
from tasks.ScheduleTasks import *

load_dotenv()
SetAPIKey(os.environ.get('PGA_TOUR_API_KEY'))

import json

# Get seasons / years that have data
years = GetYears()
mapped_years = [Year(**y) for y in years]

schedule_years = GetScheduleYears()
schedule_years_json = schedule_years['data']['scheduleYears']['years']
mapped_schedule_years = [Year(sy['queryValue'], sy['displayValue']) for sy in schedule_years_json]

# arr_schedule_years = [[sy['queryValue'], sy['displayValue']] for sy in schedule_years_json]
# CreateOrAppendCSV('data/schedule', 'schedule.csv', "w", ['year', 'displayValue'], arr_schedule_years)

schedules = []
for (index, year) in enumerate(mapped_schedule_years):
    print("{0} / {1}".format(index, len(mapped_years)))
    schedule = GetSchedule(year.year)
    mapped_schedule = Schedule(**schedule['data']['schedule'])
    schedules.append(mapped_schedule)
RunGetScheduleTasks(schedules)
# with open('data/test-data-json/schedule-2024.json', "w") as file:
#     json.dump(schedule, file)



# # Trigger data ingestion call
# for year in mapped_years:
#     GetStatCsvs(year.year)

# players = GetPlayers()
# mapped_players = [Player(**p) for p in players]

# # Run Tasks
# RunGetPlayersDirectoryTask()
# RunGetPlayerCareerProfilesTask(
#     players = mapped_players, 
#     save_career_profiles = False, 
#     save_players_achievements = False, 
#     save_players_years = False)
    
# # Clean up data files and directories
# path = os.getcwd() + '/data'
# DeleteEmptyDataFiles(path)
# DeleteEmptyDirectories(path)

