from dotenv import load_dotenv

from tour.Year import Year
from players.Player import Player
from players.player_profile_career import *

from file_helper import *
from json_data_mapping import *
from csv_helper import *
from pga_data_calls import *
from generate_csv_data import *

from tasks.player_tasks.player_career_profile_task import *
from tasks.player_tasks.players_directory_task import *
from tasks.player_tasks.player_stats_task import *

load_dotenv()
set_api_key(os.environ.get('PGA_TOUR_API_KEY'))

# Get seasons / years that have data
years = get_years()
mapped_years = [Year(**y) for y in years]

# Trigger data ingestion call
for year in mapped_years:
    get_stat_csvs(year.year)

players = get_players()
mapped_players = [Player(**p) for p in players]

# Run Tasks
run_players_directory_task()
run_player_career_profiles_task(
    players = mapped_players, 
    save_career_profiles = False, 
    save_players_achievements = False, 
    save_players_years = False)
    
# Clean up data files and directories
path = os.getcwd() + '/data'
delete_empty_data_files(path)
delete_empty_directories(path)

