import urllib.parse

url = 'https://www.pgatour.com/api/stats-download?'

params = {'timePeriod': 'THROUGH_EVENT', \
            'statsId': 186, \
            'tourCode': 'R', \
            'year': 2024 }

print(url + urllib.parse.urlencode(params))