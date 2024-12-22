from classes.courses.course import *
from data_queries.pga.courses import *

import pandas as pd

df = pd.read_csv('data/tournaments/season_tournaments.csv', sep=',', on_bad_lines='skip', dtype = str)
tournaments = df[['year', 'tournament_id']]
tournament_ids = df['tournament_id'].unique().tolist()

course_ids = set()

for index, t_id in enumerate(tournament_ids[0:1]):
        print("TournamentID: {0} ({1} / {2}) "
            .format( 
                    t_id, 
                    index,
                    len(tournament_ids)
                    ), 
            end='\r'
            )
        
        call_response = get_course_stats(t_id)
        
        json_obj = call_response['data']['courseStats']['courses']

        courses = [PGA_Course(**c) for c in json_obj]

        for c in courses:
            id = c.courseId
            if id in course_ids:
                continue
            else:
                course_ids.add(id)