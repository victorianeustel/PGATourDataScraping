from  .stat_sub_category import StatSubCategory

class StatCategory():
    def __init__(self, year, category, displayName, subCategories):
        self.year = year
        self.category = category
        self.displayName = displayName
        self.subCategories = [StatSubCategory(year, category, displayName, **sc) for sc in subCategories]

    def __str__(self):
        string_arr = [str(sc) for sc in self.subCategories]
        return "Category: {0} DisplayName: {1} SubCategories: {2}".format(self.category, self.displayName, str(string_arr))