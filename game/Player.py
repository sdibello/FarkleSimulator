
class Player:
    def __init__(self, name, handlimit, handlimitdice, OutPassDiceLimit):
        self.name = name
        self.passedHandlimitScore = handlimit
        self.passedhandimitDice = handlimitdice
        self.OutPassDiceLimit = OutPassDiceLimit
        self.FarkleCount = 0
        self.BFFarkleCount = 0
        self.score = 0
