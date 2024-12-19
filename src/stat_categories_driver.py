from data.pga.courses import *
from data.pga.stats import *

from helpers.csv_helper import *

from classes.player_stats.stat_category import *
from classes.player_stats.stat_detail import *
from classes.tour.year import *

stat_cats_header = StatDetail.header
stat_cats = []

stat_data = get_stat_details()

stat_cats_json = stat_data['data']['statDetails']['statCategories']
stat_cats_objs = [StatCategory(**c) for c in stat_cats_json]

for c in stat_cats_objs:
    for sc in c.subCategories:
        for sd in sc.stats:
            stat_cats.append(sd.ToArray())

create_or_append_csv('data/stats', 'stat_categories.csv', 'w', stat_cats_header, stat_cats)