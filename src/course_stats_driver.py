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
        # print(json_obj)
        courses = [PGA_Course(**c) for c in json_obj]
        course = courses[0]
        print(course.courseId)
        # print(courses)
        # course = PGA_Course(**json_obj[0])
        # hole = json_obj[0]['roundHoleStats'][0]['holeStats'][0]
        # print(hole)
        # hole_stat = HoleStats(holeNumber=hole['courseHoleNum'],
        #                     parValue=hole['parValue'],
        #                     yards = hole['yards'],
        #                     scoringAverage = hole['scoringAverage'],
        #                     scoringAverageDiff = hole['scoringAverageDiff'],
        #                     scoringDiffTendency = hole['scoringDiffTendency'],
        #                     eagles = hole['eagles'],
        #                     birdies = hole['birdies'],
        #                     pars = hole['pars'],
        #                     bogeys = hole['bogeys'],
        #                     doubleBogeys = hole['doubleBogey'],
        #                     rank = hole['rank'],
        #                     holeImage = hole['holeImage'],
        #                     holePickleGreenLeftToRight = hole['holePickleGreenLeftToRight'],
        #                     pinGreen = hole['pinGreen']
        #                     )
        
        # print(course.id)