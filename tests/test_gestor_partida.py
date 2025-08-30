from src.juego.gestor_partida import gestor

def test_gestor_init(mocker):
    # forzamos input a devolver "3"
    mocker.patch("builtins.input", return_value="3")
    g = gestor()
    assert len(g.jugadores) == 3  # verificamos que se crearon 3 jugadores