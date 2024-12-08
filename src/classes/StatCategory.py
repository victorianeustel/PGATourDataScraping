class StatCategory():
    def __init__(self, category, displayName, subCategories):
        self.category = category
        self.displayName = displayName
        self.subCategories = [StatSubCategory(**sc) for sc in subCategories]

    def __str__(self):
        string_arr = [str(sc) for sc in self.subCategories]
        return "Category: {0} DisplayName: {1} SubCategories: {2}".format(self.category, self.displayName, str(string_arr))
    
class StatSubCategory():
    def __init__(self, displayName, stats):
        self.displayName = displayName
        self.stats = [StatDetail(**s) for s in stats]

    def __str__(self):
        string_arr = [str(s) for s in self.stats]
        return "SubCategory - DisplayName: {0} Stats: {1}".format(self.displayName, str(string_arr))
    
class StatDetail():
    def __init__(self, statId, statTitle):
        self.statId = statId
        self.statTitle = statTitle

    def __str__(self):
        return "StatDetail - StatId: {0} StatTitle: {1}".format(self.statId, self.statTitle)