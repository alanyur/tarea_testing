from src.juego.arbitro_ronda import arbitro
from src.juego import cacho

def test_dudar(mocker):
    jugadores = [cacho.Cacho() for _ in range(2)]
    mock_cuenta = mocker.patch(
        "src.juego.contador_pintas.contador.cuenta",
        return_value=[3, 2, 1, 0, 0, 0]  # hay 3 "as", 2 "tonto"
    )
    a=arbitro()
    a.jugadores=jugadores

    resultado = a.dudar(2,"as",jugadores)  # pedimos 2 ases, y hay 3
    assert resultado is True

    # verificamos que cuenta fue llamado con los jugadores
    mock_cuenta.assert_called_once_with(jugadores)

def test_calzar(mocker):
    jugadores = [cacho.Cacho() for _ in range(2)]
    mock_cuenta = mocker.patch(
        "src.juego.contador_pintas.contador.cuenta",
        return_value=[3, 2, 1, 0, 0, 0]  # hay 3 "as", 2 "tonto"
    )
    a=arbitro()
    a.jugadores=jugadores

    resultado = a.calzar(3,"as",jugadores)  # pedimos 3 ases, y hay 3
    assert resultado is True

    # verificamos que cuenta fue llamado con los jugadores
    mock_cuenta.assert_called_once_with(jugadores)

def test_pasar_dado():
    jugadores = [cacho.Cacho() for _ in range(4)]
    a=arbitro()
    a.jugadores=jugadores
    a.pasar_dado("calzar",False,jugadores,0)
    c_dados = len(jugadores[0].dados)
    assert c_dados ==  4