import context
import sys
import pytest
from dice import dice
from score import scoreCalculate


def test_just_dice():
    ds = dice.rollDice(5)
    assert len(ds) > 0

#calcualte sets of 3
def test_calculate_score_three_sixes():
    score = scoreCalculate.calcScore([6, 6, 6, 3, 2])
    assert score == 600

def test_calculate_score_three_threes():
    score = scoreCalculate.calcScore([2, 2, 3, 3, 3])
    assert score == 300

def test_calculate_score_three_fours():
    score = scoreCalculate.calcScore([1, 4, 4, 3, 4])
    assert score == 400

def test_calculate_score_three_fives():
    score = scoreCalculate.calcScore([1, 4, 5, 5, 5])
    assert score == 500

def test_calculate_score_three_sixes():
    score = scoreCalculate.calcScore([1, 6, 5, 6, 6])
    assert score == 600

#calcualte sets of 4
def test_calculate_score_four_twos():
    score = scoreCalculate.calcScore([2, 2, 4, 2, 2])
    assert score == 400

def test_calculate_score_four_threes():
    score = scoreCalculate.calcScore([3, 2, 3, 3, 3])
    assert score == 600

def test_calculate_score_four_fours():
    score = scoreCalculate.calcScore([4, 2, 4, 4, 4])
    assert score == 800

def test_calculate_score_four_fives():
    score = scoreCalculate.calcScore([5, 5, 5, 5, 2])
    assert score == 1000

def test_calculate_score_four_sixes():
    score = scoreCalculate.calcScore([6, 6, 4, 6, 6])
    assert score == 1200

#calcualte sets of 5
def test_calculate_score_five_twos():
    score = scoreCalculate.calcScore([2,2,2,2,2])
    assert score == 800

def test_calculate_score_five_threes():
    score = scoreCalculate.calcScore([3,3,3,3,3])
    assert score == 1200

def test_calculate_score_five_fours():
    score = scoreCalculate.calcScore([4,4,4,4,4])
    assert score == 1600

def test_calculate_score_five_fives():
    score = scoreCalculate.calcScore([5,5,5,5,5])
    assert score == 2000

def test_calculate_score_five_twos():
    score = scoreCalculate.calcScore([6,6,6,6,6])
    assert score == 2400



#others
def test_calculate_score_non_straigh():
    score = scoreCalculate.calcScore([1, 4, 2, 3, 6])
    assert score == 0

def test_calculate_score_straigh_one_five():
    score = scoreCalculate.calcScore([1, 4, 2, 3, 5])
    assert score == 1500

def test_calcualte_score_nothing():
    score = scoreCalculate.calcScore([3, 5, 2, 3, 2])
    assert score == 0

def test_calcualte_score_nothing_two():
    score = scoreCalculate.calcScore([1, 5, 2, 3, 2])
    assert score == 0



