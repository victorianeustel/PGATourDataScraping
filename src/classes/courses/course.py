from .round_hole_stats import *
from .course_overview import *

class PGA_Course():
    course_tournament_header = ["tournament_id", "course_id"]
    course_header = ["course_id", "name", "course_code", "par", "yardage", "city", "state", "country"]
    
    def __init__(self,tournamentId, courseId, courseName,
                courseCode, holeDetailsAvailability, par,
                yardage, hostCourse, courseImage, roundHoleStats,
                courseOverview, shotlinkLogo):
        self.tournamentId = tournamentId
        self.courseId = courseId
        self.courseName = courseName
        self.courseCode = courseCode
        self.par = par
        self.yardage = yardage
        self.roundHoleStats = [RoundHoleStats(courseId, **rh) for rh in roundHoleStats]
        self.courseOverview = CourseOverview(**courseOverview)
        self.city = self.courseOverview.city
        self.state = self.courseOverview.state
        self.country = self.courseOverview.country
        
    def GetTournamentsCourseArray(self):
        return [self.tournamentId, self.courseId]
    
    def GetCoursesArray(self):
        return [self.courseId, self.courseName, self.courseCode, self.par, self.yardage, self.city, self.state, self.country]
