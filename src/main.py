from DownloadStatsCsvs import GetStatCsvs
from Years import GetYears
from classes.Year import Year
from helpers.JSONDataMapping import *

years = GetYears()
mapped_years = [Year(**y) for y in years]

for year in mapped_years:
    GetStatCsvs(year.year)