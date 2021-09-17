from game.FarkleGame import FarkleGame 
from game.Player import Player
from dice.dice import rollDice
from score.scoreCalculate import *
import sys

def gameloop(game):
    #main game loop
    while game.current_highscore < 10000:
        for player in game.players:
            print("turn for ", player.name)
            turnRolls = rollDice(5)
            print(turnRolls)
            turnScore = calcScore(turnRolls)
            player.score = player.score + turnScore[0]
            print("Player score total - " + str(turnScore[0]) + "(" + str(player.score) + ")" + " on " + str(turnScore[1]))
        game.calc_highest_score()




def main ():
    print("Starting Game")
    game = FarkleGame()
    gameloop(game)
    print("Ending Game")

if __name__ == "__main__":
    # execute only if run as a script
    main()