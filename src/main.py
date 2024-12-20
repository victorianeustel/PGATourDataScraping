
# from classes.tour.year import Year
# from classes.players.player import Player
# from classes.players.player_profile_career import *
# from classes.tournaments.schedule import *

# from helpers.file_helper import *
# from helpers.csv_helper import *

# from tasks.player_tasks.player_career_profile_task import *
# from tasks.player_tasks.players_directory_task import *
# from tasks.player_tasks.player_stats_task import *
# from tasks.tournament_tasks.schedule_task import *
# from tasks.merge_stats_task import *

# # Get seasons / years that have data
# # years = get_years()
# # mapped_years = [Year(**y) for y in years]

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
# run_merge_csv_groups_task()
    
# # Clean up data files and directories
# path = os.getcwd() + '/data'
# delete_empty_data_files(path)
# delete_empty_directories(path)

