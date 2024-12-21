from .stat_detail import StatDetail

class StatSubCategory():
    def __init__(self, category, categoryDisplayName, displayName, stats):
        self.displayName = displayName
        self.stats = [StatDetail(category, categoryDisplayName, displayName, **s) for s in stats]

    def __str__(self):
        string_arr = [str(s) for s in self.stats]
        return "SubCategory - DisplayName: {0} Stats: {1}".format(self.displayName, str(string_arr))