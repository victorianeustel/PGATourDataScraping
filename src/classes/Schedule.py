class Schedule():
    def __init__(self, completed, filters, seasonYear, tour, upcoming):
        self.seasonYear = seasonYear
        self.tour = tour
        self.filters = filters
        self.upcoming = [ScheduleMonth(**u) for u in upcoming]
        self.completed = [ScheduleMonth(**c) for c in completed]
        
class ScheduleMonth():
    def __init__(self, month, year, monthSort, tournaments):
        self.month = month
        self.year = year
        self.monthSort = monthSort
        self.tournaments = [Tournament(**t) for t in tournaments]

class Tournament:
    def __init__(self, tournamentName, id, beautyImage, champion, champions, championEarnings, championId, 
                city, country, countryCode, courseName, date, dateAccessibilityText, purse, sortDate, startDate, 
                state, stateCode, status, tournamentStatus, ticketsURL, tourStandingHeading, tourStandingValue, 
                tournamentLogo, display, sequenceNumber, tournamentCategoryInfo, tournamentSiteURL, useTournamentSiteURL):
        self.tournamentName = tournamentName
        self.id = id
        self.beautyImage = beautyImage
        self.champion = champion
        self.champions = [TournamentChampion(id, **tc) for tc in champions]
        self.championEarnings = championEarnings
        self.championId = championId
        self.city = city
        self.country = country
        self.countryCode = countryCode
        self.courseName = courseName
        self.date = date
        self.dateAccessibilityText = dateAccessibilityText
        self.purse = purse
        self.sortDate = sortDate
        self.startDate = startDate
        self.state = state
        self.stateCode = stateCode
        self.status = status
        self.tournamentStatus = tournamentStatus
        self.ticketsURL = ticketsURL
        self.tourStandingHeading = tourStandingHeading
        self.tourStandingValue = tourStandingValue
        self.tournamentLogo = tournamentLogo
        self.display = display
        self.sequenceNumber = sequenceNumber
        self.tournamentCategoryInfo = tournamentCategoryInfo
        self.tournamentSiteURL = tournamentSiteURL
        self.useTournamentSiteURL = useTournamentSiteURL

    def __repr__(self):
        return f"Tournament(tournamentName={self.tournamentName}, tournament_id={self.id}, city={self.city}, country={self.country}, date={self.date})"

class TournamentChampion():
    def __init__(self, tournamentId, displayName, playerId):
        self.tournamentId = tournamentId
        self.displayName = displayName
        self.playerId = playerId