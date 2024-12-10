class Year():
    def __init__(self, year, displaySeason):
        self.year = year
        self.displaySeason = displaySeason

    def __str__(self):
        return "Year: {0} DisplaySeason: {1}".format(self.year, self.displaySeason)