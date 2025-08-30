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