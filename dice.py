import random

class Dice:
    def __init__(self):
        pass
    def roll_dice(self):
        return random.randint(1,6)
    def pinta(self, value: int) -> str | None:
        pintas = {1: "As", 2: "Tonto", 3: "Tren", 4: "Cuadra", 5: "Quina", 6: "Sexto",}
        return pintas.get(value)