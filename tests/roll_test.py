import context
import sys
from dice import dice
from score import scoreCalculate


ds = dice.rollDice(5)
print("random rolls ")
print(ds)
print("score for [1, 4, 2, 3, 6]")
score = scoreCalculate.calcScore([1, 4, 2, 3, 6])
print(score)
print("score for [1, 4, 2, 3, 5]")
score = scoreCalculate.calcScore([1, 4, 2, 3, 5])
print(score)
print("score for [3, 5, 2, 3, 2]")
score = scoreCalculate.calcScore([3, 5, 2, 3, 2])
print(score)
print("score for [1, 5, 2, 3, 2]")
score = scoreCalculate.calcScore([1, 5, 2, 3, 2])
print(score)

