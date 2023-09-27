import sys, pytest
from numb3rs import validate


def test_correct():

    assert validate("1.2.3.4") == True
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True
    assert validate("100.99.9.0") == True

def test_incorrect_bytes():

    assert validate("99.99.99") == False
    assert validate("275.275.275.275") == False
    assert validate("100.10.100.10.100") == False
    assert validate("100.275.100.275") == False

def test_incorrect_values():

    assert validate("cat") == False