import csv

from classes.courses.course import *

course_data_path = "data/courses/"

tournament_courses_filename = course_data_path + "tournament_courses.csv"
courses_filename = course_data_path +"courses.csv"
course_overviews_filename = course_data_path +"course_overviews.csv"
course_hole_stats_filename = course_data_path +"course_hole_stats.csv"
course_hole_stats_summary_filename = course_data_path +"course_hole_stats_summary.csv"

def InitializeCourseCSVs():
    with open(tournament_courses_filename, "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow(PGA_Course.course_tournament_header)
        
    with open(courses_filename, "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow(PGA_Course.course_header)
        
    with open(course_overviews_filename, "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow(CourseOverviewItem.header)
        
    with open(course_hole_stats_filename, "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow(HoleStats.header)    
    
    with open(course_hole_stats_summary_filename, "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow(SummaryRow.header)

def AppendTournamentCourses(courses: list[PGA_Course]):
    with open(tournament_courses_filename, "a") as f:
        writer = csv.writer(f, delimiter=',')
        for c in courses:
            writer.writerow(c.GetTournamentsCourseArray())
            
def AppendCourses(courses: list[PGA_Course]):
    with open(courses_filename, "a") as f:
        writer = csv.writer(f, delimiter=',')
        for c in courses:
            writer.writerow(c.GetCoursesArray())
            
def AppendCoursesOverviews(courses: list[PGA_Course]):
    with open(course_overviews_filename, "a") as f:
        writer = csv.writer(f,delimiter=',')
        for c in courses:
            overview = c.courseOverview
            overview_items = overview.overviewItems
            for oi in overview_items:
                writer.writerow(oi.ToArray())
                
def AppendCourseHoleStats(courses: list[PGA_Course]):
    with open(course_hole_stats_filename, "a") as f:
        writer = csv.writer(f,delimiter=',')
        for c in courses:
            round_hole_stats = c.roundHoleStats
            for r in round_hole_stats:
                for h in r.holeStats:
                    writer.writerow(h.ToArray())
                
def AppendCourseHoleSummaryStats(courses: list[PGA_Course]):
    with open(course_hole_stats_summary_filename, "a") as f:
        writer = csv.writer(f,delimiter=',')
        for c in courses:
            for r in c.roundHoleStats:
                for h in r.summaryRow:
                    writer.writerow(h.ToArray())