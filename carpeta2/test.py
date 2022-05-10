import pytest
from Examenescrito03032021 import nota


def test_examenteorico03032021():
    lista = [1, 4.5, 8]
    assert nota(lista) == [33, 33, 33]