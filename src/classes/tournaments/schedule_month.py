from .tournament import *

class ScheduleMonth():
    def __init__(self, month, year, monthSort, tournaments):
        self.month = month
        self.year = year
        self.monthSort = monthSort
        self.tournaments = [Tournament(month, year, **t) for t in tournaments]
