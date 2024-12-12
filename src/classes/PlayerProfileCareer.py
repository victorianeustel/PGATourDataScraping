class PlayerProfileCareer(): 
    def __init__(self, playerId, tourCode, events, wins, winsTitle, internationalWins, majorWins, cutsMade, runnerUp, second, third, top10, top25, years, officialMoney, tourPills,achievements,tables):
        self.playerId = playerId
        self.tourCode = tourCode
        self.events = events
        self.wins = wins
        self.winsTitle = winsTitle
        self.internationalWins = internationalWins
        self.majorWins = majorWins
        self.cutsMade = cutsMade
        self.runnerUp = runnerUp
        self.second = second
        self.third = third
        self.top10 = top10
        self.top25 = top25
        self.years = years
        self.officialMoney = officialMoney
        self.tourPills = tourPills
        self.achievements = achievements
        self.tables = tables
        
    # Get array of property names
    def GetListOfPropertyNames(self):
        # keys = self.__dict__.keys()
        # keyList = [*keys]
        # to_be_removed = {'years', 'tourPills', 'achievements', 'tables'}
        # [item for item in keyList if item not in to_be_removed ]
        # return keyList
        
        arr =  ['playerId',
            'tourCode',
            'events',
            'wins',
            'winsTitle',
            'internationalWins',
            'majorWins',
            'cutsMade',
            'runnerUp',
            'second',
            'third',
            'top10',
            'top25',
            'officialMoney']
        return arr
    
    def ToArray(self):
        arr =  [self.playerId,
            self.tourCode,
            self.events,
            self.wins,
            self.winsTitle,
            self.internationalWins,
            self.majorWins,
            self.cutsMade,
            self.runnerUp,
            self.second,
            self.third,
            self.top10,
            self.top25,
            self.officialMoney]
        
        return arr