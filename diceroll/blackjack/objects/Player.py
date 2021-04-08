
class Player:
    def __init__(self):
        self.total = 0

    def addToTotal(self, roll):
        self.total += roll

    def getTotal(self):
        return self.total