import pytest
from unittest.mock import Mock, patch
from src.juego.arbitro_ronda import arbitro
from src.juego.gestor_partida import gestor
from src.juego.contador_pintas import Contador

def test_integracion(mocker):
    
    # Mock para la entrada de cantidad de jugadores
    mocker.patch("builtins.input", return_value="2")
    
    # Mock para que el jugador 1 empiece (índice 0)
    mocker.patch("random.randint", return_value=0)
    
    g = gestor()
    assert len(g.jugadores) == 2
    
    # Verificar que inicia el jugador 1 (índice 0)
    assert g.turno_actual == 0
    
    # Mockear los dados de los jugadores
    g.jugadores[0].dados = [3, 3, 3, 3, 5] 
    g.jugadores[1].dados = [3, 3, 2, 4, 6] 
    
    a = arbitro()
    a.jugadores = g.jugadores
    
    # Mockear el contador de pintas para que devuelva valores específicos para hacerlo determinista 
    with patch.object(Contador, 'cuenta') as mock_cuenta:
        mock_cuenta.return_value = [0, 0, 6, 0, 0, 0]  # [as, tonto, tren, cuadra, quinta, sexta]
        
        # Jugador 2 duda de la apuesta de 4 trenes
        # La duda es INCORRECTA porque hay MÁS de 4 trenes (hay 6)
        resultado_duda = a.dudar(4, "tren", g.jugadores)
        assert resultado_duda is True  # Dudaste mal
        
        # Verificar que se llamó al contador con los jugadores correctos
        mock_cuenta.assert_called_once_with(g.jugadores)
    
    # Jugador 2 pierde un dado por dudar mal
    dados_iniciales_jugador2 = len(g.jugadores[1].dados)
    a.pasar_dado("dudar", False, g.jugadores, 1) 
    
    # Verificar que el jugador 2 perdió un dado
    assert len(g.jugadores[1].dados) == dados_iniciales_jugador2 - 1
    
    # Verificar que el jugador 1 mantiene todos sus dados
    assert len(g.jugadores[0].dados) == 5

def test_integracion_duda_correcta(mocker):
   # Mock para la entrada de cantidad de jugadores
    mocker.patch("builtins.input", return_value="2")
    mocker.patch("random.randint", return_value=0)
    
    g = gestor()
    a = arbitro()
    a.jugadores = g.jugadores
    
    with patch.object(Contador, 'cuenta') as mock_cuenta:
        # Total: solo 2 trenes (menos de los 4 apostados)
        mock_cuenta.return_value = [0, 0, 2, 0, 0, 0] # [as, tonto, tren, cuadra, quinta, sexta]
        
        # Jugador 2 duda de la apuesta de 4 trenes
        resultado_duda = a.dudar(4, "tren", g.jugadores)
        assert resultado_duda is False  # Duda bien
        
        mock_cuenta.assert_called_once_with(g.jugadores)
     
    dados_iniciales_jugador1 = len(g.jugadores[0].dados)
    a.pasar_dado("dudar", True, g.jugadores, 1)  # Jugador 1 (anterior) pierde un dado
    
    assert len(g.jugadores[0].dados) == dados_iniciales_jugador1 - 1