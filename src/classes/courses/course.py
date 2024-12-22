from .round_hole_stats import *
from .course_overview import *

class PGA_Course():
    
    def __init__(self,tournamentId, courseId, courseName,
                courseCode, holeDetailsAvailability, par,
                yardage, hostCourse, courseImage, roundHoleStats,
                courseOverview, shotlinkLogo):
        self.courseId = courseId
        self.courseName = courseName
        self.courseCode = courseCode
        self.par = par
        self.yardage = yardage
        self.courseImage = courseImage   
        self.roundHoleStats = [RoundHoleStats(**rh) for rh in roundHoleStats]
        self.courseOverview = CourseOverview(**courseOverview)