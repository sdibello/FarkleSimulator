
class Player:
    def __init__(self, name, handlimit, handlimitdice, OutPassDiceLimit):
        self.name = name
        self.passedHandlimitScore = handlimit
        self.passedhandimitDice = handlimitdice
        self.OutPassDiceLimit = OutPassDiceLimit
        self.FarkleCount = 0
        self.BFFarkleCount = 0
        self.score = 0

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

    def player_judge_pass(self, score, available_dice):
        if score > self.passedHandlimitScore:
            return True
        elif available_dice >= self.passedhandimitDice:
            return True
        else:
            return False
