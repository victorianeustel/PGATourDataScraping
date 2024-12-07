class StatCategory():
    def __init__(self, category, displayName, subCategories):
        self.category = category
        self.displayName = displayName
        self.subCategories = [StatSubCategory(**sc) for sc in subCategories]

    def __str__(self):
        return "{0} {1}".format(self.category, self.displayName)
    
class StatSubCategory():
    def __init__(self, displayName, stats):
        self.displayName = displayName
        self.stats = [StatDetail(**s) for s in stats]

    def __str__(self):
        return "{0} ,{1}".format(self.displayName, self.stats)
    
class StatDetail():
    def __init__(self, statId, statTitle):
        self.statId = statId
        self.statTitle = statTitle

    def __str__(self):
        return "{0} {1}".format(self.statId, self.statTitle)