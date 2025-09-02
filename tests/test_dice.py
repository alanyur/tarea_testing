from unittest import mock
import pytest
from dice import Dice

def test_roll_dice():
    dice = Dice()
    roll_dice = dice.roll_dice()
    assert roll_dice in [1,2,3,4,5,6]

@pytest.mark.parametrize("_input, expected", [(1, "As"), (2, "Tonto"), (3, "Tren"), (4, "Cuadra"), (5, "Quina"), (6, "Sexto")])
@mock.patch("dice.Dice.roll_dice")
def test_pinta(mock_roll_dice, _input, expected):
    dice = Dice()
    assert dice.pinta(_input) == expected