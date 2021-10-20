import context
import sys
import pytest
from dice import dice
from score import scoreCalculate


def test_just_five_dice():
    ds = dice.rollDice(5)
    assert len(ds) > 0

def test_just_four_dice():
    ds = dice.rollDice(4)
    assert len(ds) == 4

def test_just_three_dice():
    ds = dice.rollDice(3)
    assert len(ds) == 3

def test_just_two_dice():
    ds = dice.rollDice(2)
    assert len(ds) == 2

def test_just_one_dice():
    ds = dice.rollDice(1)
    assert len(ds) == 1

#calcualte sets of 3
def test_calculate_score_three_sixes_plus():
    score = scoreCalculate.calcScore([6, 6, 6, 4, 2])
    assert score == (600, [6, 6, 6], [4, 2])

def test_calculate_score_three_sixes_less_then_five():
    score = scoreCalculate.calcScore([6, 6, 6, 2])
    assert score == (600, [6, 6, 6], [2])

def test_calculate_score_three_sixes_less_then_four():
    score = scoreCalculate.calcScore([6, 6, 6])
    assert score == (600, [6, 6, 6], [])

def test_calculate_score_2_sixes():
    score = scoreCalculate.calcScore([6, 6])
    assert score == (0, [], [6, 6])

def test_calculate_score_three_threes():
    score = scoreCalculate.calcScore([2, 4, 3, 3, 3])
    assert score == (300, [3, 3, 3], [2, 4]) 

def test_calculate_score_three_fours():
    score = scoreCalculate.calcScore([2, 4, 4, 3, 4])
    assert score == (400, [4, 4, 4], [2, 3]) 

def test_calculate_score_three_fives():
    score = scoreCalculate.calcScore([2, 4, 5, 5, 5])
    assert score == (500, [5, 5, 5], [2, 4])

def test_calculate_score_three_sixes():
    score = scoreCalculate.calcScore([1, 6, 5, 6, 6])
    assert score == (750, [6, 6, 6, 5, 1], [])

#calcualte sets of 4
def test_calculate_score_four_twos():
    score = scoreCalculate.calcScore([2, 2, 4, 2, 2])
    assert score == (400, [2, 2, 2, 2], [4])

def test_calculate_score_four_twos_not_full():
    score = scoreCalculate.calcScore([2, 2, 2, 2])
    assert score == (400, [2, 2, 2, 2], [])

def test_calculate_score_3_2s():
    score = scoreCalculate.calcScore([2, 2, 2])
    assert score == (200, [2, 2, 2], [])

def test_calculate_score_2_2s():
    score = scoreCalculate.calcScore([2, 2])
    assert score == (0, [], [2, 2])

def test_calculate_score_1_2s():
    score = scoreCalculate.calcScore([2])
    assert score == (0, [], [2])


def test_calculate_score_four_threes():
    score = scoreCalculate.calcScore([3, 2, 3, 3, 3])
    assert score ==  (600, [3, 3, 3, 3], [2])

def test_calculate_score_four_fours():
    score = scoreCalculate.calcScore([4, 2, 4, 4, 4])
    assert score == (800, [4, 4, 4, 4], [2])

def test_calculate_score_four_fives():
    score = scoreCalculate.calcScore([5, 5, 5, 5, 2])
    assert score == (1000, [5, 5, 5, 5], [2])

def test_calculate_score_four_sixes():
    score = scoreCalculate.calcScore([6, 6, 4, 6, 6])
    assert score == (1200, [6, 6, 6, 6], [4])

#calcualte sets of 5
def test_calculate_score_five_ones():
    score = scoreCalculate.calcScore([1,1,1,1,1])
    assert score == (4000, [1, 1, 1, 1, 1], [])

def test_calculate_score_five_twos():
    score = scoreCalculate.calcScore([2,2,2,2,2])
    assert score == (800, [2, 2, 2, 2, 2], [])

def test_calculate_score_five_threes():
    score = scoreCalculate.calcScore([3,3,3,3,3])
    assert score == (1200, [3, 3, 3, 3, 3], [])

def test_calculate_score_five_fours():
    score = scoreCalculate.calcScore([4,4,4,4,4])
    assert score == (1600, [4, 4, 4, 4, 4], [])

def test_calculate_score_4_fours():
    score = scoreCalculate.calcScore([4,4,4,4])
    assert score == (800, [4, 4, 4, 4], [])

def test_calculate_score_five_fives():
    score = scoreCalculate.calcScore([5,5,5,5,5])
    assert score == (2000, [5, 5, 5, 5, 5], [])

def test_calculate_score_five_sixes():
    score = scoreCalculate.calcScore([6,6,6,6,6])
    assert score == (2400, [6, 6, 6, 6, 6], [])

def test_calculate_score_two_fives():
    score = scoreCalculate.calcScore([5,5])
    assert score == (100, [5, 5], [])

def test_calculate_score_one_five():
    score = scoreCalculate.calcScore([5])
    assert score == (50, [5], [])

def test_calculate_score_1():
    score = scoreCalculate.calcScore([1])
    assert score == (100, [1], [])

def test_calculate_score_1_1():
    score = scoreCalculate.calcScore([1,1])
    assert score == (200, [1, 1], [])

def test_calculate_score_1_5():
    score = scoreCalculate.calcScore([1,5])
    assert score == (150, [5, 1], [])

#others
def test_calculate_score_non_straigh():
    score = scoreCalculate.calcScore([1, 4, 2, 3, 6])
    assert score == (100, [1], [4, 2, 3, 6])

def test_calculate_score_straigh_one_five():
    score = scoreCalculate.calcScore([1, 4, 2, 3, 5])
    assert score == (1500, [1, 4, 2, 3, 5], [])

def test_calculate_score_straigh_2_6():
    score = scoreCalculate.calcScore([6, 4, 2, 3, 5])
    assert score == (1500, [6, 4, 2, 3, 5], [])


def test_calcualte_score_five():
    score = scoreCalculate.calcScore([3, 5, 2, 3, 2])
    assert score == (50, [5], [3, 2, 3, 2])

def test_calcualte_score_nothing_one_five():
    score = scoreCalculate.calcScore([1, 5, 2, 3, 2])
    assert score == (150, [5, 1], [2, 3, 2])

def test_calcualte_score_nothing():
    score = scoreCalculate.calcScore([4, 6, 2, 3, 2])
    assert score == (0, [], [4, 6, 2, 3, 2])

def test_calcualte_score_one_one_five():
    score = scoreCalculate.calcScore([1, 1, 3, 5, 2])
    assert score == (250, [5, 1, 1], [3, 2]) 

def test_calcualte_score_one_one_one_five():
    score = scoreCalculate.calcScore([1, 1, 3, 5, 1])
    assert score == (1050, [1, 1, 1, 5], [3])

def test_calcualte_score_three_three_three_five():
    score = scoreCalculate.calcScore([3, 2, 3, 5, 3])
    assert score == (350, [3, 3, 3, 5], [2]) 

def test_calcualte_score_3_3_3_5_1():
    score = scoreCalculate.calcScore([3, 1, 3, 5, 3])
    assert score == (450, [3, 3, 3, 5, 1], [])

def test_calcualte_score_1_1_5():
    score = scoreCalculate.calcScore([1, 1, 3, 5, 3])
    assert score == (250, [5, 1, 1], [3, 3])

def test_calcualte_score_weird_straight():
    score = scoreCalculate.calcScore([4, 1, 5, 6, 3])
    assert score == (150, [5, 1], [4, 6, 3])

def test_calcualte_score_weird_two_straight():
    score = scoreCalculate.calcScore([4, 1, 5, 6, 2])
    assert score == (150, [5, 1], [4, 6, 2])

def test_calcualte_score_weird_three_straight():
    score = scoreCalculate.calcScore([3, 1, 5, 6, 2])
    assert score == (150, [5, 1], [3, 6, 2])

def test_calcualte_score_weird_four_straight():
    score = scoreCalculate.calcScore([6, 3, 5, 4, 2])
    assert score == (1500, [6, 3, 5, 4, 2], [])