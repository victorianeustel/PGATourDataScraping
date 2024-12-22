from .course_overview_item import *

class CourseOverview():
    def __init__(self, id, image, name, city, state, country, overview):
        self.id = id
        self.name = name
        self.city = city
        self.state = state
        self.country = country
        self.overviewItems = [CourseOverviewItem(id, **item) for item in overview]
        