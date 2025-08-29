import random

class Dice:
    def __init__(self):
        self._value = 0
    def roll_dice(self):
        self._value = random.randint(1,6)
        return self._value
    def pinta(self, val: int) -> str | None:
        pintas = {1: "As", 2: "Tonto", 3: "Tren", 4: "Cuadra", 5: "Quina", 6: "Sexto",}
        return pintas.get(val)
    def get_value(self):
        return self._value