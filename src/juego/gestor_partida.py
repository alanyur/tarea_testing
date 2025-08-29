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

    def turno(self):
        self.turno_actual = (self.turno_actual + 1) % len(self.jugadores)
        print(f"Turno del jugador {self.turno_actual + 1}")
        ###aqui va todo lo de los turnos

    def un_dado(self):
        k=len(self.jugadores)
        for i in range (k):
            if len(self.jugadores[self.turno_actual].dados)==1:
                print("te queda un dado")
                return True
            else:
                return False
