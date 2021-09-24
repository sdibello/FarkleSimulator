
class Player:
    def __init__(self, name, handlimit, handlimitdice, OutPassDiceLimit):
        self.name = name
        self.passedHandlimitScore = handlimit
        self.passedhandimitDice = handlimitdice
        self.OutPassDiceLimit = OutPassDiceLimit
        self.FarkleCount = 0
        self.BFFarkleCount = 0
        self.score = 0
        self.passToBrackets = []


    def load_passToBrackets(self, brackets):
        self.passToBrackets = brackets

    def player_turn_end(self):
        # TODO
        #when a player turn ends.  
        # 1. - check high score, and if win , start endgame
        # 2. - 
        print("turn end")

    def player_turn_begin(self):
        #when a player turn begins.  
        # TODO
        # 1. move roll/pass decision here so it can be tested.
        print("turn debgin")

    def player_judge_accept_passed(self, score, available_dice):
        for b in self.passToBrackets:
            if score >= b.low_score and available_dice >= b.available_dice:
                return True
        return False
