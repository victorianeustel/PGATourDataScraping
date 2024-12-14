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
        self.age = playerBio['age']
        self.education = playerBio['education']
        self.turnedPro = playerBio['turnedPro']
        # self.playerBio = PlayerBio(**playerBio)
        
    def ToArray(self):
        return [self.id, self.isActive, self.firstName, self.lastName, 
                self.shortName, self.displayName, self.alphaSort, 
                self.country, self.countryFlag, self.headshot, 
                self.age, self.education, self.turnedPro]
    
class PlayerBio():
    def __init__(self, id, age, education, turnedPro):
        self.playerId = id
        self.age = age
        self.education = education
        self.turnedPro = turnedPro