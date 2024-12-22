from .hole_stats import *
from .summary_row import *

class RoundHoleStats():
    def __init__(self, courseId, roundHeader, roundNum, live, holeStats):
        self.courseId = courseId
        self.holeNumber = roundHeader
        self.roundNum = roundNum
        self.holeStats = [HoleStats(courseId = courseId,
                                    roundNumber = roundNum, 
                            holeNumber=hole['courseHoleNum'],
                            parValue=hole['parValue'],
                            yards = hole['yards'],
                            scoringAverage = hole['scoringAverage'],
                            scoringAverageDiff = hole['scoringAverageDiff'],
                            scoringDiffTendency = hole['scoringDiffTendency'],
                            eagles = hole['eagles'],
                            birdies = hole['birdies'],
                            pars = hole['pars'],
                            bogeys = hole['bogeys'],
                            doubleBogeys = hole['doubleBogey'],
                            rank = hole['rank'],
                            holeImage = hole['holeImage'],
                            holePickleGreenLeftToRight = hole['holePickleGreenLeftToRight'],
                            pinGreen = hole['pinGreen']
                            ) for hole in holeStats if hole['__typename'] == "CourseHoleStats"]
        self.summaryRow = [SummaryRow(
                            courseId = courseId,
                            roundNumber = roundNum,
                            rowType=hole['rowType'],
                            par=hole['par'],
                            scoringAverageDiff = hole['scoringAverageDiff'],
                            scoringDiffTendency = hole['scoringDiffTendency'],
                            yardage = hole['yardage'],
                            scoringAverage = hole['scoringAverage'],
                            eagles = hole['eagles'],
                            birdies = hole['birdies'],
                            pars = hole['pars'],
                            bogeys = hole['bogeys'],
                            doubleBogeys = hole['doubleBogey'],
                            ) for hole in holeStats if hole['__typename'] == "SummaryRow"]
