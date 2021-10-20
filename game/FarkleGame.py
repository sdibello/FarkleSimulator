from game.Player import Player
from dice.dice import *
from score.scoreCalculate import *

class FarkleGame:
    players = []

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self.winning_score = 10000
        self.current_highscore = 0
        self.rounds = 0
        steve = Player('Steve', 300, 2, 3)
        paul = Player('Paul', 450, 2, 2)
        jerry = Player('Jerry', 250, 3, 3)
        tina = Player('Tina', 350, 3, 2)
        #steve = object(name = 'Steve', handlimit = '300', order=1, BigFatFarkle=0, Farkle=0, open=False)
        #paul = object(name = 'Paul', handlinit = '500', order=2, BigFatFarkle=0, Farkle=0, open=False)
        #jerry = object(name = 'Jerry', handlinit = '250', order=3, BigFatFarkle=0, Farkle=0, open=False)
        #ina = object(name = 'Tina', handlimit = '350', order=4, BigFatFarkle=0, Farkle=0, open=False)
        self.players.append(steve)
        self.players.append(paul)
        self.players.append(jerry)
        self.players.append(tina)

    def calc_highest_score(self):
        current_highscore = 0
        for player in self.players:
            if player.score > current_highscore:
                current_highscore = player.score
        self.current_highscore = current_highscore
        return self.current_highscore
    
    def print_scores(self):
        #creating a new list here, to maintain the order of players in the original list.
        newlist = sorted(self.players, key=lambda x: x.score, reverse=True)
        print(" ----------- Round {0} ------------- ".format(self.rounds))
        for p in newlist:
            print("{0} has {1} ".format(p.name, p.score))
        print(" ----------------------------------- ".format(self.rounds))

    def print_statistics(self):
        #creating a new list here, to maintain the order of players in the original list.
        newlist = sorted(self.players, key=lambda x: x.score, reverse=True)
        print(" ----------- Stats ------------- ".format(self.rounds))
        for p in newlist:
            print("{0} has {1} - {2} farkles, - {3} Big Fat Farkles ".format(p.name, p.score, p.FarkleCount, p.BFFarkleCount))
        print(" -------------------------------- ".format(self.rounds))


    def players_turn(self, player, in_score, in_available_dice, debug_flag):
        player_turn_score = 0
        diceToRoll = in_available_dice

        if debug_flag:
            print("turn for " + player.name + " < passed " + str(in_available_dice) + "-" + str(in_score)  )

        # This should be pulled out into a function as well
        # detect if the score passed to me is above my limit 
        if in_score >= player.passedHandlimitScore:
            player_turn_score = in_score
            diceToRoll = in_available_dice
            if in_available_dice == 0:
                diceToRoll = 5
        
        #turn loop
        reRollFlag = True
        while (reRollFlag):
            #roll
            turnRolls = rollDice(diceToRoll)
            if debug_flag:
                print("-- " + str(turnRolls))
            activeRolls = calcScore(turnRolls)  ## score, scored-dice, remaining-dice
            roll_scored_dice = len(activeRolls[1])
            roll_remaining_dice = len(activeRolls[2])
            roll_score = activeRolls[0]
            #split reroll logic out into method.
            # Farkle Detection and Resolution
            # Make a function so it's testable
            if (roll_scored_dice == 0):
                if diceToRoll == 5:
                    player.BFFarkleCount += 1
                    print("-- !!!!!!! Big Fat Farkle - (" + str(player.BFFarkleCount) + ")" )
                else:
                    player.FarkleCount += 1
                    print("-- !!!!!!! Farkle - (" + str(player.FarkleCount) + ")" )
                player_turn_score = 0
                passedDice = [5,5,5,5,5]
                passedScore = 0
            else:
                #Player score roll-up , dice remaining, score pass-along
                player_turn_score = player_turn_score + roll_score
                print("-- Score total - {0}-{1}-{2} on {3}".format(str(roll_score), str(player_turn_score), str(player.score), str(activeRolls[1])))
                passedScore = player_turn_score
                passedDice = activeRolls[2]
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
            if (len(passedDice) == 0) and (passedScore > 0):
                reRollFlag = True
                diceToRoll = 5
            elif (len(passedDice) == 5) and (passedScore == 0):
                reRollFlag = False
            elif (len(passedDice)) < player.OutPassDiceLimit:
                reRollFlag = False
                player.score = player.score + player_turn_score
                print("> score " + str(player_turn_score) + " for a total of " + str(player.score))
            elif (len(passedDice)) >= player.OutPassDiceLimit:
                reRollFlag = True
                diceToRoll = len(passedDice)
            else:
                reRollFlag = False
            
        return out_score, out_available_dice

    def game_turn_end(self):
        # TODO
        #when a player turn ends.  
        # 1. - check high score, and if win , start endgame
        # 2. - 
        print("turn end")

    def game_turn_begin(self):
        #when a player turn begins.  
        # TODO
        # 1. move roll/pass decision here so it can be tested.
        print("turn debgin")
