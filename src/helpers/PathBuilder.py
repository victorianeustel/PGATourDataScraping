import urllib.parse

# https://www.pgatour.com/_next/data/pgatour-prod-1.71.3/en/stats/detail.json?statId=138&stat_id=138
url = 'https://www.pgatour.com/api/stats-download?'

def get_stats_path(statsId: int, year: int = 2024, tourCode: str = 'R', timePeriod:str = 'THROUGH_EVENT'):
    params = {
        'timePeriod': timePeriod, 
        'statsId': statsId, 
        'tourCode': tourCode, 
        'year': year 
        }
    return url + urllib.parse.urlencode(params)
