import csv
from classes.tournaments.schedule import * 

tournaments_header = ['month','year','id','tournamentName','champion',
                'championEarnings','championId','city','country','countryCode',
                'courseName','date','purse','startDate', 'state','stateCode',
                'status','tournamentStatus','tourStandingHeading','tourStandingValue',
                'tournamentSiteURL' ]

def run_tournaments_task(schedules: list[Schedule]):
    with open('data/tournaments/tournaments.csv', "w", newline='\n') as csvfile:
            writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
            writer.writerow(tournaments_header)
            for schedule in schedules:
                for month in schedule.upcoming:
                    for tournament in month.tournaments:
                        writer.writerow(tournament.ToArray())    
                for month in schedule.completed:
                    for tournament in month.tournaments:
                        writer.writerow(tournament.ToArray())            