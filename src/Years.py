from classes.Year import Year
from helpers.JSONDataMapping import *

years = GetYears()
mapped_years = [Year(**y) for y in years]

for year in mapped_years:
    print(str(year))