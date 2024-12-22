class CourseOverviewItem():
    header = ["course_id", "label", "value", "detail", "secondary_detail"]
    
    def __init__(self, course_id, label, value, detail, secondaryDetail, wide, smallCopy):
        self.course_id = course_id
        self.label = label
        self.value = value
        self.detail = detail
        self.secondaryDetail = secondaryDetail
        
    def ToArray(self):
        return [self.course_id, self.label, self.value, self.detail, self.secondaryDetail]