from plates import is_valid


def test_true():

    assert is_valid("CS50") == True
    assert is_valid("CS") == True

def test_number_placement():

    assert is_valid("CS50P") == False
    assert is_valid("CSP50") == True

def test_alnum_char():
    assert is_valid("CS50.p") == False
    assert is_valid("500") == False

def test_length():
    assert is_valid("H") == False
    assert is_valid("OUTTATIME") == False
    assert is_valid("CSP500") == True

def test_zero_place():
    assert is_valid("CS05") == False