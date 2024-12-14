import urllib.parse

# https://www.pgatour.com/_next/data/pgatour-prod-1.71.3/en/stats/detail.json?statId=138&stat_id=138

# Build path for stat CSV download endpoint
def get_stats_path(statsId: int, year: int, tourCode: str = 'R', timePeriod:str = 'THROUGH_EVENT'):
    params = {
        'timePeriod': timePeriod, 
        'statsId': statsId, 
        'tourCode': tourCode, 
        'year': year 
        }
    path = 'https://www.pgatour.com/api/stats-download?' + urllib.parse.urlencode(params)
    return path

# path = 'https://www.usga.org/Home/GetClubsActionResult?clubCity=&clubState=&clubName=&assocNum=19'
def get_usga_courses(clubCity: str = "", clubState: str = "", clubName: str = "", assocNum: str = ""):
    url = 'https://www.usga.org/Home/GetClubsActionResult?'
    params = {
        'clubCity': clubCity, 
        'clubState': clubState, 
        'clubName': clubName, 
        'assocNum': assocNum 
        }
    path = url + urllib.parse.urlencode(params)
    return path
