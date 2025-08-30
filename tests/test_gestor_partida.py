from src.juego.gestor_partida import gestor

def test_gestor_init(mocker):
    # forzamos input a devolver "3"
    mocker.patch("builtins.input", return_value="3")
    g = gestor()
    assert len(g.jugadores) == 3  # verificamos que se crearon 3 jugadores

def test_iniciar_juego(mocker):
    # forzamos input a devolver "2"
    mocker.patch("builtins.input", return_value="2")
    mocker.patch("random.randint", return_value=1)  # forzamos random a devolver 1
    g = gestor()
    # forzamos random.randint a devolver 1
    assert g.turno_actual == 1


def test_turno(mocker):
    mocker.patch("builtins.input", return_value="2")
    mocker.patch("random.randint", return_value=1)  # forzamos random a devolver 1
    g = gestor()
    g.turno()  # turno actual pasa de 1 a 0 (porque hay 2 jugadores)
    assert g.turno_actual == 0


def test_un_dado(mocker):
    mocker.patch("builtins.input", return_value="2")
    mocker.patch("random.randint", return_value=1)  # forzamos random a devolver 1
    g = gestor()
    g.jugadores[1].dados = [3]  # forzamos que el jugador 1 tenga un solo dado
    resultado = g.un_dado()  # turno actual es 1
    assert resultado is True