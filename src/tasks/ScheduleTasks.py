from helpers.JSONDataMapping import *
from helpers.CSVHelper import *
from helpers.PGADataCalls import *
from classes.Schedule import *
from classes.Year import *

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

def RunGetScheduleTasks():
    
    schedule_years = GetScheduleYears()
    schedule_years_json = schedule_years['data']['scheduleYears']['years']
    mapped_schedule_years = [Year(sy['queryValue'], sy['displayValue']) for sy in schedule_years_json]

    schedules = []
    for (index, year) in enumerate(mapped_schedule_years):
        print("{0} / {1}".format(index, len(mapped_schedule_years)))
        schedule = GetSchedule(year.year)
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
