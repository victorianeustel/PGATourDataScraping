from classes.courses.course import *
from helpers.driver_helpers.courses_helper import *
from data_queries.pga.courses import *

import pandas as pd

df = pd.read_csv('data/tournaments/season_tournaments.csv', sep=',', on_bad_lines='skip', dtype = str)
tournaments = df[['year', 'tournament_id']]
tournament_ids = df['tournament_id'].unique().tolist()

course_ids = set()

InitializeCourseCSVs()

for index, t_id in enumerate(tournament_ids):
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

        # for c in courses:
        if len(courses) <= 0: continue
        
        c = courses[0]
        id = c.courseId
        # Add courses for tournaments
        AppendTournamentCourses(courses)

        if id in course_ids:
            continue
        else:
            #Add courses
            AppendCourses(courses)
            
            # Add course overviews
            AppendCoursesOverviews(courses)
            
            # Add round hole stats 
            AppendCourseHoleStats(courses)
            
            # Add course hole stats summary row
            AppendCourseHoleSummaryStats(courses)
            
            course_ids.add(id)
                
                