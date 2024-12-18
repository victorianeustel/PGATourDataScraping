from data.pga.courses import *
from data.pga.stats import *

from helpers.csv_helper import *

from classes.tour.year import *

stat_data = get_stat_details()

stat_years_json = stat_data['data']['statDetails']['yearPills']
stat_years_objs = [Year(**y) for y in stat_years_json]
stat_years = [y.ToArray() for y in stat_years_objs]
stat_years_header = Year.header

create_or_append_csv('data/stats', 'stat_years.csv', 'w', stat_years_header, stat_years)