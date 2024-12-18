from helpers.csv_helper import *

class Year():
    header = ['Year', 'DisplayName']
    
    def __init__(self, year, displaySeason):
        self.year = year
        self.displaySeason = displaySeason

    def __str__(self):
        return "Year: {0} DisplaySeason: {1}".format(self.year, self.displaySeason)
    
    def ToArray(self):
        return [self.year, self.displaySeason]
    
    # def AppendToCSV(self, file_path):
    #     create_or_append_csv(path=file_path,
    #                         fileWritingType='a',
    #                         content_rows=[self.ToArray()])