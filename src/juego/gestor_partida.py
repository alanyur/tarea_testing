import random
from src.juego import cacho
class gestor:
    def __init__(self):
        cantidad_jugadores=int(input("ingrese la cantidad de jugadores (2-5): "))
        while cantidad_jugadores <2 or cantidad_jugadores>5:
            cantidad_jugadores=int(input("ingrese la cantidad de jugadores (2-5): "))
        self.jugadores = [cacho.Cacho() for i in range(cantidad_jugadores)]
        self.iniciar_juego()

    def iniciar_juego(self):
        # Elegir al azar quién comienza
        self.turno_actual = random.randint(0, len(self.jugadores) - 1)
        print(f"Inicia jugador {self.turno_actual + 1}")

   
  
