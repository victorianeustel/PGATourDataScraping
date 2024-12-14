from players.player_achievement import *
from tour.tour import TourPill
from players.player_year import PlayerYear

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
        self.years = [PlayerYear(playerId, **y) for y in years]
        self.officialMoney = officialMoney
        self.tourPills = [TourPill(**t) for t in tourPills]
        self.achievements = [PlayerAchievement(playerId, **a) for a in achievements]
        self.tables = tables
        
    # Get array of property names
    def GetListOfPropertyNames(self):
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