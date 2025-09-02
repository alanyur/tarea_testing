import pytest

from src.juego.contador_pintas import Contador
from src.juego.cacho import Cacho
from unittest.mock import Mock

def test_contar_dados_por_pinta_ronda_normal():
    #jugadores=[Cacho(dados=[1,1,5,5,3]),Cacho(dados=[2,2,4,6,1]),Cacho(dados=[3,3,3,4,4]),Cacho(dados=[1,2,3,4,5])]
    jugadores=[Mock(dados=[1,1,5,5,3]),Mock(dados=[2,2,4,6,1]),Mock(dados=[3,3,3,4,4]),Mock(dados=[1,2,3,4,5])]
    contador=Contador()
    resultado=contador.cuenta(jugadores)
    assert resultado[0] == 4
    assert resultado[1] == 7
    assert resultado[2] == 9
    assert resultado[3] == 8
    assert resultado[4] == 7
    assert resultado[5] == 5

def test_contar_dados_por_pinta_ronda_especial():
    #jugadores=[Cacho(dados=[1,1,5,5,3]),Cacho(dados=[2,2,4,6,1]),Cacho(dados=[3,3,3,4,4]),Cacho(dados=[1,2,3,4,5])]
    jugadores=[Mock(dados=[1,1,5,5,3]),Mock(dados=[2,2,4,6,1]),Mock(dados=[3,3,3,4,4]),Mock(dados=[1,2,3,4,5])]
    contador=Contador()
    contador.ronda_especial=True
    resultado=contador.cuenta(jugadores)
    assert resultado[0] == 4
    assert resultado[1] == 3
    assert resultado[2] == 5
    assert resultado[3] == 4
    assert resultado[4] == 3  
    assert resultado[5] == 1  