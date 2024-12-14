from .schedule_month import *

class Schedule():
    def __init__(self, completed, filters, seasonYear, tour, upcoming):
        self.seasonYear = seasonYear
        self.tour = tour
        self.filters = filters
        self.upcoming = [ScheduleMonth(**u) for u in upcoming]
        self.completed = [ScheduleMonth(**c) for c in completed]
        


