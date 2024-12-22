class SummaryRow():
    header = ["course_id","round_number",  "par", "scoring_average_diff",
            "scoring_diff_tendency", "yardage", "scoring_average",
            "eagles", "birdies", "pars", "bogeys", "double_bogeys"]
    
    
    def __init__(self,courseId, roundNumber, rowType, par, scoringAverageDiff, scoringDiffTendency, yardage, scoringAverage, eagles, birdies, pars, bogeys, doubleBogeys):
        self.courseId = courseId
        self.roundNumber = roundNumber,
        self.rowType = rowType
        self.par = par
        self.scoringAverageDiff = scoringAverageDiff
        self.scoringDiffTendency = scoringDiffTendency
        self.yardage = yardage
        self.scoringAverage = scoringAverage
        self.eagles = eagles
        self.birdies = birdies
        self.pars = pars
        self.bogeys = bogeys
        self.doubleBogeys = doubleBogeys
        
    def ToArray(self):
        return [self.courseId, self.roundNumber[0],  self.par, self.scoringAverageDiff,
                self.scoringDiffTendency, self.yardage, self.scoringAverage,
                self.eagles, self.birdies, self.pars, self.bogeys,
                self.doubleBogeys]