class contador:
    def cuenta(self,jugadores):
        cantidad_dados=[0,0,0,0,0,0]
        for j in range(len(jugadores)):
            for k in range(len(jugadores[j].dados)):
                if(jugadores[j].dados[k].total=="as"):
                    cantidad_dados[0]=+1
                elif(jugadores[j].dados[k].total=="tonto"):
                    cantidad_dados[1]=+1
                elif(jugadores[j].dados[k].total=="tren"):
                    cantidad_dados[2]=+1
                elif(jugadores[j].dados[k].total=="cuadra"):
                    cantidad_dados[3]=+1
                elif(jugadores[j].dados[k].total=="quinta"):
                    cantidad_dados[4]=+1
                elif(jugadores[j].dados[k].total=="sexta"):
                    cantidad_dados[5]=+1
        return cantidad_dados
    def dados_totales(self,jugadores):
        total=0
        for j in range(len(jugadores)):
            total+=len(jugadores[j].dados)
        return total
###Cuenta cuantas hay en realidad
