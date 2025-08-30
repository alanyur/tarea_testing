class Contador:
    def __init__(self):
        self.ronda_especial = False

    def cuenta(self, jugadores):
        cantidad_dados = [0] * 6  
        for jugador in jugadores:
            for dado in jugador.dados:
                if dado == 1 and not self.ronda_especial:
                    for i in range(len(cantidad_dados)):
                        cantidad_dados[i] += 1
                else:
                    cantidad_dados[dado - 1] += 1
        return cantidad_dados

