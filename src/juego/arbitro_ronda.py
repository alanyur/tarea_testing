from src.juego import contador_pintas
class arbitro:

###tengo que hacer la condicion para que alguien gane la partida


    def dudar(self,cantidad,pinta,jugadores):
        pintas={
                "as":int(0),
                "tonto":int(1),
                "tren":int(2),
                "cuadra":int(3),
                "quinta":int(4),
                "sexta":int(5)
            }
        cantidad_dados=contador_pintas.contador().cuenta(jugadores)
        indice=pintas[pinta]
        if cantidad_dados[indice] >= cantidad:
            return True ###dudaste bien
        else:
            return False ###dudaste mal
        

    def calzar(self,cantidad,pinta,jugadores):
        pintas={
                "as":int(0),
                "tonto":int(1),
                "tren":int(2),
                "cuadra":int(3),
                "quinta":int(4),
                "sexta":int(5)
            }
        cantidad_dados=contador_pintas.contador().cuenta(jugadores)
        indice=pintas[pinta]
        if cantidad_dados[indice] == cantidad:
            return True ###calzaste bien
        else:
            return False ###calzaste mal


    def pasar_dado(self,string,boolean,jugadores,k):
        if string=="calzar" and boolean==True:
            jugadores[k].dados.pop()
        elif string=="calzar" and boolean==False:
            jugadores[k].dados.pop()
        elif string=="dudar" and boolean==True:
            jugadores[k-1].dados.pop()
        elif string=="dudar" and boolean==False:
            jugadores[k].dados.pop()

    def validar_calzar(self,cantidad,jugadores,k):
        pass