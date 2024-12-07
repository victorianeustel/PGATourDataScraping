import urllib.parse

url = 'https://www.pgatour.com/api/stats-download?'


# Stats Id
## Putting:SG - 02564
## Scoring:SG - 02675
## Rankings - 186
## SG: tee to green - 02674
## Consecutive birdies / eagles streak - 02673
## Consecutive birdies streak - 02672
## FedEx Standings - 02671

params = {'timePeriod': 'THROUGH_EVENT', \
            'statsId': 186, \
            'tourCode': 'R', \
            'year': 2024 }

print(url + urllib.parse.urlencode(params))

# https://www.pgatour.com/_next/data/pgatour-prod-1.71.3/en/stats/detail.json?statId=138&stat_id=138
