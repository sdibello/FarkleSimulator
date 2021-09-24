import context
import sys
import pytest
from dice import dice
from score import scoreCalculate
from game.Player import Player


def test_judge_300():
    p = Player('test', 350, 3, 2)
    result = p.player_judge_pass(300, 3)
    assert result == True

def test_judge_350():
    p = Player('test', 350, 3, 2)
    result = p.player_judge_pass(350, 3)
    assert result == True

def test_judge_400():
    p = Player('test', 400, 3, 2)
    result = p.player_judge_pass(350, 3)
    assert result == True