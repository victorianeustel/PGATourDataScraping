from .tournament_champion import *

class Tournament:
    def __init__(self, month, year, tournamentName, id, beautyImage, champion, champions, championEarnings, championId, 
                city, country, countryCode, courseName, date, dateAccessibilityText, purse, sortDate, startDate, 
                state, stateCode, status, tournamentStatus, ticketsURL, tourStandingHeading, tourStandingValue, 
                tournamentLogo, display, sequenceNumber, tournamentCategoryInfo, tournamentSiteURL, useTournamentSiteURL):
        self.month = month
        self.year = year
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
    
    def ToArray(self):
        return [self.month,
                self.year,
                self.id,
                self.tournamentName,
                self.champion,
                self.championEarnings,
                self.championId,
                self.city,
                self.country,
                self.countryCode,
                self.courseName,
                self.date,
                self.purse,
                self.startDate,
                self.state,
                self.stateCode,
                self.status,
                self.tournamentStatus,
                self.tourStandingHeading,
                self.tourStandingValue,
                self.tournamentSiteURL ]
            