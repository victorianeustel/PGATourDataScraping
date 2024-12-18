class StatDetail():
    header = ['stat_id', 'stat_title', 'category', 'category_name', 'subcategory_name']
    
    def __init__(self, statCategory, statCategoryName, 
                subCategoryName, statId, statTitle):
        self.statId = statId
        self.statTitle = statTitle
        self.statCategory = statCategory
        self.statCategoryName = statCategoryName
        self.subcategoryName = subCategoryName

    def __str__(self):
        return "StatDetail - StatId: {0} StatTitle: {1}".format(self.statId, self.statTitle)
    
    def ToArray(self):
        return [self.statId, self.statTitle, self.statCategory, self.statCategoryName, self.subcategoryName]