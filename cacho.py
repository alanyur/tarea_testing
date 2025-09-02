from dice import Dice

class Cacho:
    dados = [0]*5
    def __init__(self):
        self.dados = [Dice() for i in range(5)]

    def agitar(self):
        resultado = [self.dados[i].roll_dice() for i in range(5)]
        return resultado

    def mostrar(self):
        resultado = [self.dados[i].get_value() for i in range(len(self.dados))]
        return resultado