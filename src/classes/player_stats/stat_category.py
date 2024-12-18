from  .stat_sub_category import StatSubCategory

class StatCategory():
    def __init__(self, category, displayName, subCategories):
        self.category = category
        self.displayName = displayName
        self.subCategories = [StatSubCategory(category, displayName, **sc) for sc in subCategories]

    def __str__(self):
        string_arr = [str(sc) for sc in self.subCategories]
        return "Category: {0} DisplayName: {1} SubCategories: {2}".format(self.category, self.displayName, str(string_arr))