class Validador:
    def __init__(self):
        self.pinta_actual = None
        self.cantidad_actual = None
        self.primera_apuesta = True

    def validar_apuesta(self, nueva_pinta, nueva_cantidad):

        hay_apuesta_previa = self.pinta_actual is not None and self.cantidad_actual is not None
        #Primera apuesta 
        if not hay_apuesta_previa:
            if nueva_pinta == 1:
                return False
            self.pinta_actual = nueva_pinta
            self.cantidad_actual = nueva_cantidad
            self.primera_apuesta = False
            return True

        #Cambio a ases 
        if nueva_pinta == 1 and self.pinta_actual != 1:
            mitad = (self.cantidad_actual // 2) + 1
            if nueva_cantidad >= mitad and nueva_cantidad != self.cantidad_actual:
                self.pinta_actual = nueva_pinta
                self.cantidad_actual = nueva_cantidad
                self.primera_apuesta = False
                return True
            return False

        #Salir de ases 
        if self.pinta_actual == 1 and nueva_pinta != 1:
            minimo = (self.cantidad_actual * 2) + 1
            if nueva_cantidad >= minimo:
                self.pinta_actual = nueva_pinta
                self.cantidad_actual = nueva_cantidad
                self.primera_apuesta = False
                return True
            return False

        #Subida normal
        if nueva_cantidad < self.cantidad_actual:
            return False
        if nueva_cantidad == self.cantidad_actual and nueva_pinta <= self.pinta_actual:
            return False

        #Todo bien
        self.pinta_actual = nueva_pinta
        self.cantidad_actual = nueva_cantidad
        self.primera_apuesta = False
        return True
