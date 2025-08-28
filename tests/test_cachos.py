import pytest
from cacho import Cacho
from dice import Dice

def test_cacho_creacion_dados():
    # Confirmar si existen las 5 instancias de dados al iniciar el juego con los cachos
    cacho = Cacho()
    for d in cacho.dados:
        assert isinstance(d, Dice)


def test_agitar_dados():
    # Confirmar si al agitar el cacho, los 5 dados dan valores entre 1 a 6
    cacho = Cacho()
    numeros = cacho.agitar()
    print('\n', "resultado = ", numeros, end = '\n')
    for numero in numeros:
        assert numero in [1,2,3,4,5,6]