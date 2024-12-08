from helpers.PathBuilder import *
import requests

path = get_stats_path(statsId= '02394')

x = requests.get(path)
print(path)
print(x.content)

with open("data/ingested/myfile.csv", "w") as file:
    file.writelines(x.text)