import random

class Dice:
    def __init__(self):
        pass
    def roll_dice(self):
        return random.randint(1,6)
    def pinta(self, int):
        match (int):
            case 1:
                return "As"
            case 2:
                return "Tonto"
            case 3:
                return "Tren"
            case 4:
                return "Cuadra"
            case 5:
                return "Quina"
            case 6:
                return "Sexto"
            case _:
                return None