
class Player:
    def __init__(self, name, handlimit, handlimitdice, OutPassLimit):
        self.name = name
        self.passedHandlimitScore = handlimit
        self.passedhandimitDice = handlimitdice
        self.OutPassLimit = OutPassLimit
        self.FarkleCount = 0
        self.BFFarkleCount = 0
        self.score = 0
