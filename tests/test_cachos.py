import pytest
from cacho import Cacho
from dice import Dice

def test_cacho_creacion_dados():
    cacho = Cacho()
    for d in cacho.dados:
        assert isinstance(d, Dice)