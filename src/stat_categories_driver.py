from data.pga.courses import *
from data.pga.stats import *

from helpers.csv_helper import *

from classes.player_stats.stat_category import *
from classes.player_stats.stat_detail import *
from classes.tour.year import *

# year = 2024
base_stat_data = get_stat_details(2024)
stat_years_json = base_stat_data['data']['statDetails']['yearPills']
stat_years_objs = [Year(**y) for y in stat_years_json]

stat_cats = []

for y in stat_years_objs:
    year = int(y.year)
    stat_data = get_stat_details(year)

    stat_cats_json = stat_data['data']['statDetails']['statCategories']
    stat_cats_objs = [StatCategory(year, **c) for c in stat_cats_json]
    stat_cats_header = StatDetail.header

    for c in stat_cats_objs:
        print('Category: ' + c.displayName)
        for sc in c.subCategories:
            print('Subcategory: ' + sc.displayName)
            print (sc.stats)
            for sd in sc.stats:
                # print(sd.ToArray())
                stat_cats.append(sd.ToArray())

create_or_append_csv('data/stats', 'stat_categories.csv', 'w', stat_cats_header, stat_cats)