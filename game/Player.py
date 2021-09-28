from score.scoreCalculate import calcScore
from dice.dice import rollDice

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
            if score >= b.low_score and score <= b.high_score:
                if available_dice >= b.available_dice:
                    return True
        return False
    
    def player_turn_loop(self, passed_score, passedDice):

        reRollFlag = True
        print("turn for " + self.name + " < passed " + str(passedDice) + "-" + str(passed_score)  )
        
        acceptPassedFlag = self.player_judge_accept_passed(passed_score, passedDice)
        if acceptPassedFlag == True:
            player_turn_score = passed_score
        else:
            player_turn_score = 0
            passedDice = 5
        
        #turn loop
        while (reRollFlag):
            turnRolls = rollDice(passedDice)
            print("-- " + str(turnRolls))
            activeRolls = calcScore(turnRolls)  ## score, scored-dice, remaining-dice
            roll_scored_dice = len(activeRolls[1])
            roll_remaining_dice = len(activeRolls[2])
            roll_score = activeRolls[0]
            # split reroll logic out into method.
            # Farkle Detection and Resolution
            # Make a function so it's testable
            if (roll_scored_dice == 0):
                if passedDice == 5:
                    self.BFFarkleCount += 1
                    print("-- !!!!!!! Big Fat Farkle - (" + str(self.BFFarkleCount) + ")" )
                else:
                    self.FarkleCount += 1
                    print("-- !!!!!!! Farkle - (" + str(self.FarkleCount) + ")" )
                player_turn_score = 0
                passedDice = 5
                passedScore = 0
            else:
                #Player score roll-up , dice remaining, score pass-along
                player_turn_score = player_turn_score + roll_score
                print("-- Score total-{0} turn total-{1} player total-{2} on {3}".format(str(roll_score), str(player_turn_score), str(self.score), str(activeRolls[1])))
                passedScore = player_turn_score
                passedDice = len(activeRolls[2])
                if passedDice == 0:
                    passedDice = 5
            #TODO MVP Notes
            # 1. decide to keep passed or reset
            # 2. roll & Score ( return all possible score iterations)
            # 3. farkle detection
            # 4. decide which score to keep
            # 5. decide pass / reroll - loop at #2
            # 6. log score
            # 7. pass
            
            # figure out how to store so I can run AI on it.
            # End Game - relist players once someone has decided to end the game
            #TODO nice to have
            # 1. Opening score limit
            # 2. change the way players decide based on  their score, and the highest score.
            # roll pass / reroll decision 
            # make a function so it's testable
            if (passedDice == 0) and (passedScore > 0):
                reRollFlag = True
                diceToRoll = 5
            elif (passedDice == 5) and (passedScore == 0):
                reRollFlag = False
            elif passedDice < self.OutPassDiceLimit:
                reRollFlag = False
                self.score = self.score + player_turn_score
                print("> score " + str(player_turn_score) + " for a total of " + str(self.score))
            elif passedDice >= self.OutPassDiceLimit:
                reRollFlag = True
            else:
                reRollFlag = False
        
        return player_turn_score, passedDice        
