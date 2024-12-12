class Player():
    def __init__(self, id, isActive, firstName, lastName, shortName, displayName, alphaSort, country, countryFlag, headshot, playerBio):
        self.id = id
        self.isActive = isActive
        self.firstName = firstName
        self.lastName = lastName
        self.shortName = shortName
        self.displayName = displayName
        self.alphaSort = alphaSort
        self.country = country
        self.countryFlag = countryFlag
        self.headshot = headshot
        self.playerBio = PlayerBio(**playerBio)

    def __str__(self):
        return "Year: {0} DisplaySeason: {1}".format(self.year, self.displaySeason)
    
class PlayerBio():
    def __init__(self, id, age, education, turnedPro):
        self.playerId = id
        self.age = age
        self.education = education
        self.turnedPro = turnedPro