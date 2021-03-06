import context
import sys
import pytest
from dice import dice
from score import scoreCalculate
from game.Player import Player
from game.score_bracket import score_bracket

@pytest.fixture(scope='session')
def load_normal_player():
    one = score_bracket(250,350,4)
    two = score_bracket(400,500,3)
    three = score_bracket(550,850,2)
    four = score_bracket(900,99999,1)
    p = Player('test',350,3,2)
    p.passToBrackets.append(one)
    p.passToBrackets.append(two)
    p.passToBrackets.append(three)
    p.passToBrackets.append(four)
    pytest.normal_player = p

def test_judge_normal_150(load_normal_player):
    result = pytest.normal_player.player_judge_accept_passed(150, 3)
    assert result == False

def test_judge_normal_300(load_normal_player):
    result = pytest.normal_player.player_judge_accept_passed(300, 3)
    assert result == False

def test_judge_normal_350(load_normal_player):
    result = pytest.normal_player.player_judge_accept_passed(350, 4)
    assert result == True

def test_judge_normal_400(load_normal_player):
    result = pytest.normal_player.player_judge_accept_passed(400, 3)
    assert result == True

def test_judge_normal_550(load_normal_player):
    result = pytest.normal_player.player_judge_accept_passed(550, 2)
    assert result == True

def test_judge_normal_550_One(load_normal_player):
    result = pytest.normal_player.player_judge_accept_passed(550, 1)
    assert result == False

def test_judge_normal_900(load_normal_player):
    result = pytest.normal_player.player_judge_accept_passed(900, 2)
    assert result == True

def test_judge_normal_900(load_normal_player):
    result = pytest.normal_player.player_judge_accept_passed(1100, 1)
    assert result == True

def test_judge_normal_200_2(load_normal_player):
    result = pytest.normal_player.player_judge_accept_passed(200, 2)
    assert result == False

def test_judge_normal_300_1(load_normal_player):
    result = pytest.normal_player.player_judge_accept_passed(300, 2)
    assert result == False

def test_judge_normal_2000_1(load_normal_player):
    result = pytest.normal_player.player_judge_accept_passed(2000, 1)
    assert result == True

def test_judge_normal_2000_2(load_normal_player):
    result = pytest.normal_player.player_judge_accept_passed(2000, 2)
    assert result == True


def test_judge_normal_1100_1(load_normal_player):
    result = pytest.normal_player.player_judge_accept_passed(1100, 1)
    assert result == True