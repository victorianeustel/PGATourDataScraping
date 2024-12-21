from data_queries.pga.courses import *
from data_queries.pga.stats import *

from helpers.csv_helper import *

from classes.tournaments.tournament_pill import *

tournament_years = []

with open('data/stats/stat_years.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    reader.__next__()
    for row in reader:
        tournament_years.append(int(row[0]))

create_or_append_csv('data/tournaments', 'season_tournaments.csv', 'w', header=TournamentPill.header)

for year in tournament_years:
    print(year)
    stat_data = get_stat_details(year=year, statId="120")
    stat_tournaments_json = stat_data['data']['statDetails']['tournamentPills']
    stat_tournaments_objs = [TournamentPill(year, **t) for t in stat_tournaments_json]
    stat_tournaments = [y.ToArray() for y in stat_tournaments_objs]
    create_or_append_csv('data/tournaments', 'season_tournaments.csv', 'a', content_rows=stat_tournaments)

