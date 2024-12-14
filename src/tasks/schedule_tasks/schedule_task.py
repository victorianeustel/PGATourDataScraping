from helpers.json_data_mapping import *
from helpers.csv_helper import *
from helpers.pga_data_calls import *
from classes.Schedule import *
from classes.tour.year import *

tournaments_header = ['month',
                'year',
                'id',
                'tournamentName',
                'champion',
                'championEarnings',
                'championId',
                'city',
                'country',
                'countryCode',
                'courseName',
                'date',
                'purse',
                'startDate',
                'state',
                'stateCode',
                'status',
                'tournamentStatus',
                'tourStandingHeading',
                'tourStandingValue',
                'tournamentSiteURL' ]

def run_schedule_tasks():
    
    schedule_years = get_schedule_years()
    schedule_years_json = schedule_years['data']['scheduleYears']['years']
    mapped_schedule_years = [Year(sy['queryValue'], sy['displayValue']) for sy in schedule_years_json]

    schedules = []
    for (index, year) in enumerate(mapped_schedule_years):
        print("{0} / {1}".format(index, len(mapped_schedule_years)))
        schedule = get_schedule(year.year)
        mapped_schedule = Schedule(**schedule['data']['schedule'])
        schedules.append(mapped_schedule)
    
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
