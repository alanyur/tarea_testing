from dice import Dice

class Cacho:
    dados = [0]*5
    def __init__(self):
        self.dados = [Dice() for i in range(5)]

    def agitar(self):
        return [1,2,3,4,5,6]

    def mostrar_ocultar(self):
        pass