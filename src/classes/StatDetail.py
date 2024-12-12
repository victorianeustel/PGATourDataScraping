class StatDetail():
    def __init__(self, statId, statTitle):
        self.statId = statId
        self.statTitle = statTitle

    def __str__(self):
        return "StatDetail - StatId: {0} StatTitle: {1}".format(self.statId, self.statTitle)