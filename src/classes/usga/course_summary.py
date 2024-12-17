from helpers.csv_helper import *

class USGA_CourseSummary():
    header = ['course_id', 'facility_name', 'course_name', 'city', 'state', 'course_details_path']
    csv_path = 'data/usga'
    csv_file_name = 'usga_courses.csv'
    
    def __init__(self, courseId, facilityName, courseName, city, state, courseDetailsPath):
        self.courseId = courseId
        self.facilityName = facilityName
        self.courseName = courseName
        self.city = city
        self.state = state
        self.courseDetailsPath = courseDetailsPath
        
    def ToArray(self):
        return [self.courseId, self.facilityName, self.courseName, 
                self.city, self.state, self.courseDetailsPath]
    
    def AddToCSV(self):
        create_or_append_csv(path=self.csv_path,
                            fileName= self.csv_file_name,
                            fileWritingType='a',
                            content_rows=[self.ToArray()])