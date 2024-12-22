class HoleStats():
    header = ['course_id',
            'round_number'
            'hole_number',
            'par_value',
            'yards',
            'scoring_average',
            'scoring_average_diff',
            'scoring_average_tendency',
            'eagles',
            'birdies',
            'pars',
            'bogeys',
            'double_bogeys',
            'rank',
            'hole_image',
            'hole_pickle_green_left_to_right'
        ]
    
    def __init__(self, courseId, roundNumber, holeNumber, parValue, yards, scoringAverage,
                scoringAverageDiff, scoringDiffTendency, eagles, birdies,
                pars, bogeys, doubleBogeys, rank, holeImage, holePickleGreenLeftToRight,
                pinGreen):
        self.courseId = courseId
        self.roundNumber = roundNumber
        self.holeNumber = holeNumber
        self.parValue = parValue
        self.yards = yards
        self.scoringAverage = scoringAverage
        self.scoringAverageDiff = scoringAverageDiff
        self.scoringAverageTendency = scoringDiffTendency
        self.eagles = eagles
        self.birdies = birdies
        self.pars = pars
        self.bogeys = bogeys
        self.doubleBogeys = doubleBogeys
        self.rank = rank
        self.holeImage = holeImage
        self.holePickleGreenLeftToRight = holePickleGreenLeftToRight
        # self.pinGreen = PinGreen(**pinGreen)
    
    def ToArray(self):
        return [self.courseId, 
                self.roundNumber,
            self.holeNumber,
            self.parValue,
            self.yards,
            self.scoringAverage,
            self.scoringAverageDiff,
            self.scoringAverageTendency,
            self.eagles,
            self.birdies,
            self.pars,
            self.bogeys,
            self.doubleBogeys,
            self.rank,
            self.holeImage,
            self.holePickleGreenLeftToRight
        ]