class PlayerYear:
    def __init__(self, playerId, cutsMade, displaySeason, events, officialMoney, second, standingsPoints, standingsRank, third, top10, top25, tourCode, wins, withdrawn, year):
        self.playerId = playerId
        self.year = year
        self.cutsMade = cutsMade
        self.displaySeason = displaySeason
        self.events = events
        self.officialMoney = officialMoney
        self.second = second
        self.standingsPoints = standingsPoints
        self.standingsRank = standingsRank
        self.third = third
        self.top10 = top10
        self.top25 = top25
        self.tourCode = tourCode
        self.wins = wins
        self.withdrawn = withdrawn
        
    def ToArray(self):
        return [
            self.playerId,
            self.year,
            self.cutsMade,
            self.displaySeason,
            self.events,
            self.officialMoney,
            self.second,
            self.standingsPoints,
            self.standingsRank,
            self.third,
            self.top10,
            self.top25,
            self.tourCode,
            self.wins,
            self.withdrawn
        ]