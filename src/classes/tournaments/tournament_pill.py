class TournamentPill():
    header = ['year', 'tournament_id', 'tournament_name']
    
    def __init__(self, year, tournamentId, displayName):
        self.year = year
        self.tournamentId = tournamentId
        self.tournamentName = displayName
        
    def ToArray(self):
        return [self.year, self.tournamentId, self.tournamentName]
    
    