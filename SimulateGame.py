from game.FarkleGame import FarkleGame 
from game.Player import Player
from dice.dice import rollDice
from score.scoreCalculate import *
import sys


def gameloop(game):
    #main game loop
    passedScore = 0
    passedDice = []
    turnRolls = []
    while game.current_highscore < 10000:

        #players loop
        for player in game.players:
            player_turn_score = 0
            diceToRoll = 5
            reRollFlag = True
            print("turn for " + player.name + " < passed " + str(len(passedDice)) + "-" + str(passedScore)  )

            if passedScore >= player.passedHandlimitScore:
                player_turn_score = passedScore
                diceToRoll = len(passedDice)
                if len(passedDice) == 0:
                    diceToRoll = 5
            
            #turn loop
            while (reRollFlag):

                turnRolls = rollDice(diceToRoll)
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

        # every round hits here.
        basic_round_end(game)

def basic_round_end(game):
    game.rounds += 1
    game.print_scores()
    game.calc_highest_score()

def turn_roll(game):
    # comming soon
    print("soon")

def main ():
    print("Starting Game")
    game = FarkleGame()
    gameloop(game)
    print("Ending Game")

if __name__ == "__main__":
    # execute only if run as a script
    main()