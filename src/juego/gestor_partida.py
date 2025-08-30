import random
from src.juego import cacho
class gestor:
    def __init__(self):
        cantidad_jugadores=int(input("ingrese la cantidad de jugadores (2-5): "))
        while cantidad_jugadores <2 or cantidad_jugadores>5:
            cantidad_jugadores=int(input("ingrese la cantidad de jugadores (2-5): "))
        self.jugadores = [cacho.Cacho() for i in range(cantidad_jugadores)]
        

    
