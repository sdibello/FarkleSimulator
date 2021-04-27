import context
import sys
from dice import dice
from score import scoreCalculate


ds = dice.rollDice(5)
print(ds)
score = scoreCalculate.calcScore([3, 5, 2, 3, 2])
print(score)

