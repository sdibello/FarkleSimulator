from game.FarkleGame import FarkleGame 
from game.Player import Player
from dice.dice import rollDice
from score.scoreCalculate import *
import sys


def gameloop(game):
    #main game loop
    passedScore = 0
    turnRolls = []
    player_turn_score = 0
    passedDice = 5
    turnCount = 0
    while game.current_highscore < 10000:

        #players loop
        for player in game.players:
            turnCount += 1
            turn_result =player.player_turn_loop(passedScore, passedDice)
            passedScore = turn_result[0]
            passedDice = turn_result[1]
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
    game.print_statistics()
    print("Ending Game")

if __name__ == "__main__":
    # execute only if run as a script
    main()