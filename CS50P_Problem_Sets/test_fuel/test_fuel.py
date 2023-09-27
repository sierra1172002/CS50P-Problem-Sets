import pytest
from fuel import convert, gauge

def test_correct():

    assert convert("1/4") == 25
    assert convert("1/3") == 33

def test_valueerror():

    with pytest.raises(ValueError):
        convert("three/four")

    with pytest.raises(ValueError):
        convert("4/3")

def test_zerodiverror():

    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_E():

    assert gauge(1) == "E"

def test_F():
    assert gauge(99) == "F"

def test_percentage():
    assert gauge(50) == "50%"
