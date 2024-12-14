from helpers.CSVHelper import *
from helpers.PGADataCalls import *
def RunGetScheduleYearsTask():
    schedule_years = GetScheduleYears()
    schedule_years_json = schedule_years['data']['scheduleYears']['years']
    
    arr_schedule_years = [[sy['queryValue'], sy['displayValue']] for sy in schedule_years_json]
    CreateOrAppendCSV('data/schedule', 'schedule.csv', "w", ['year', 'displayValue'], arr_schedule_years)

