from helpers.csv_helper import *
from helpers.pga_data_calls import *

def run_get_schedule_years_task():
    schedule_years = get_schedule_years()
    schedule_years_json = schedule_years['data']['scheduleYears']['years']
    
    arr_schedule_years = [[sy['queryValue'], sy['displayValue']] for sy in schedule_years_json]
    create_or_append_csv('data/schedule', 'schedule.csv', "w", ['year', 'displayValue'], arr_schedule_years)

