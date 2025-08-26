from dice import Dice

def test_roll_dice():
    dice = Dice()
    roll_dice = dice.roll_dice()
    assert roll_dice in [1,2,3,4,5,6]

