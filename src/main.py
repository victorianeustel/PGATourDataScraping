from dotenv import load_dotenv

from classes.tour.year import Year
from classes.players.player import Player
from classes.players.player_profile_career import *
from classes.tournaments.schedule import *

from helpers.file_helper import *
from helpers.json_data_mapping import *
from helpers.csv_helper import *
from helpers.pga_data_calls import *

from tasks.player_tasks.player_career_profile_task import *
from tasks.player_tasks.players_directory_task import *
from tasks.player_tasks.player_stats_task import *
from tasks.tournament_tasks.schedule_task import *

load_dotenv()
set_api_key(os.environ.get('PGA_TOUR_API_KEY'))

# # Get seasons / years that have data
# years = get_years()
# mapped_years = [Year(**y) for y in years]

# # Trigger data ingestion call
# for year in mapped_years:
#     get_stat_csvs(year.year)

# players = get_players()
# mapped_players = [Player(**p) for p in players]

# # Run Tasks
# run_schedule_tasks()
# run_players_directory_task()
# run_player_career_profiles_task(
#     players = mapped_players, 
#     save_career_profiles = False, 
#     save_players_achievements = False, 
#     save_players_years = False)
    
# # Clean up data files and directories
# path = os.getcwd() + '/data'
# delete_empty_data_files(path)
# delete_empty_directories(path)

from tasks.sample_data_task import *

# course_stat_overviews = get_course_stat_overviews(2023)
# write_sample_data('course_stat_overviews', course_stat_overviews)

# course_stat_details = get_course_stat_details(2023)
# write_sample_data('course_stat_details', course_stat_details)

# stats_overview = get_stats_overview(2023)
# write_sample_data('stats_overview', stats_overview)
    

# tournaments = get_tournaments([
#         "R2024551",
#         "R2024088",
#         "S2024588",
#         "R2024088",
#         "Y2024016"
#     ])
# write_sample_data('tournaments', tournaments)


# tournament_past_results = get_tournaments_past_results('R2023003', 19320)
# write_sample_data('tournament_past_results', tournament_past_results)

from tasks.merge_stats_task import *

run_merge_csv_groups_task()

# test = 'data/stats/2010/points_rankings/points/%_of_potential_pts_won_fedexcup_playoffs.csv'

# print(test.split('/')[2])