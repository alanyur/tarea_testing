from dice import Dice

class Cacho:
    dados = [0]*5
    def __init__(self):
        for i in range(5):
            self.dados[i] = Dice()

    def agitar(self):
        pass

    def mostrar_ocultar(self):
        pass