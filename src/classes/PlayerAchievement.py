class PlayerAchievement():
    def __init__(self, playerId, title, value):
        self.playerId = playerId
        self.title = title
        self.value = value
        
    def ToArray(self):
        return [
            self.playerId,
            self.title,
            self.value
        ]