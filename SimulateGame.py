from game.FarkleGame import FarkleGame 
from game.Player import Player
from dice.dice import rollDice
from score.scoreCalculate import *
import sys

def gameloop(game):
    #main game loop
    while game.current_highscore < 10000:
        passedDice = []
        turnRolls = []
        passedScore = 0
        for player in game.players:
            player_turn_score = 0
            print("turn for " + player.name + " passed " + str(passedDice) + "(" + str(passedScore) + ")" )

            if passedScore >= player.passedHandlimitScore:
                player_turn_score = passedScore
                turnRolls = rollDice(len(passedDice))
            else:
                turnRolls = rollDice(5)

            print(turnRolls)
            activeRolls = calcScore(turnRolls)

            if (len(activeRolls[1]) == 0):
                print("farkle")
                player_turn_score = 0
                passedDice = [5,5,5,5,5]
                passedScore = 0
            else:
                player_turn_score = player_turn_score + activeRolls[0]
                player.score = player.score + player_turn_score
                print("Player score total - " + str(player_turn_score) + " (" + str(player.score) + ") " + " on " + str(activeRolls[1]))
                passedScore = player_turn_score
                passedDice = activeRolls[2]
        game.calc_highest_score()




def main ():
    print("Starting Game")
    game = FarkleGame()
    gameloop(game)
    print("Ending Game")

if __name__ == "__main__":
    # execute only if run as a script
    main()