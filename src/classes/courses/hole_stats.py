class HoleStats():
    header = ['holeNumber',
            'parValue',
            'yards',
            'scoringAverage',
            'scoringAverageDiff',
            'scoringAverageTendency',
            'eagles',
            'birdies',
            'pars',
            'bogeys',
            'doubleBogeys',
            'rank',
            'holeImage',
            'holePickleGreenLeftToRight'
        ]
    
    def __init__(self, holeNumber, parValue, yards, scoringAverage,
                scoringAverageDiff, scoringDiffTendency, eagles, birdies,
                pars, bogeys, doubleBogeys, rank, holeImage, holePickleGreenLeftToRight,
                pinGreen):
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
        return [self.holeNumber,
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