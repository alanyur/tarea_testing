import pytest
from src.juego.validador import Validador

def test_subir_pinta_o_cantidad():
    validador=Validador()
    validador.pinta_actual=2
    validador.cantidad_actual=3
    nueva_pinta=5
    nueva_cantidad=5
    validado=validador.validar_apuesta(nueva_pinta,nueva_cantidad)
    assert validado == True
def test_no_subir_pinta():
    validador=Validador()
    validador.pinta_actual=2
    validador.cantidad_actual=3
    nueva_pinta=1
    nueva_cantidad=3
    validado=validador.validar_apuesta(nueva_pinta,nueva_cantidad)
    assert validado == False
def test_no_subir_cantidad():
    validador=Validador()
    validador.pinta_actual=2
    validador.cantidad_actual=3
    nueva_pinta=2
    nueva_cantidad=2
    validado=validador.validar_apuesta(nueva_pinta,nueva_cantidad)
    assert validado == False

def test_cambiar_a_ases_bien():
    validador=Validador()
    validador.pinta_actual=2
    validador.cantidad_actual=3
    nueva_pinta=1
    nueva_cantidad=2
    validado=validador.validar_apuesta(nueva_pinta,nueva_cantidad)
    assert validado == True

def test_cambiar_a_ases_mal():
    validador=Validador()
    validador.pinta_actual=2
    validador.cantidad_actual=3
    nueva_pinta=1
    nueva_cantidad=1
    validado=validador.validar_apuesta(nueva_pinta,nueva_cantidad)
    assert validado == False

def test_salir_de_ases_bien():
    validador=Validador()
    validador.pinta_actual=1
    validador.cantidad_actual=3
    nueva_pinta=2
    nueva_cantidad=7
    validado=validador.validar_apuesta(nueva_pinta,nueva_cantidad)
    assert validado == True

def test_salir_de_ases_mal():
    validador=Validador()
    validador.pinta_actual=1
    validador.cantidad_actual=3
    nueva_pinta=2
    nueva_cantidad=3
    validado=validador.validar_apuesta(nueva_pinta,nueva_cantidad)
    assert validado == False

def test_primera_apuesta_valida():
    validador=Validador()
    nueva_pinta=3
    nueva_cantidad=2
    validado=validador.validar_apuesta(nueva_pinta,nueva_cantidad)
    assert validado == True
def test_primera_apuesta_invalida():
    validador=Validador()
    nueva_pinta=1
    nueva_cantidad=5
    validado=validador.validar_apuesta(nueva_pinta,nueva_cantidad)
    assert validado == False