from bank import value


def test_hello():

    assert value("hello") == 0
    assert value("HELLO") == 0

def test_hello_phrase():

    assert value("Hello, David") == 0
    assert value("How are you doing?") == 20
    assert value("What's happening?") == 100

def test_h_absent():

    assert value("greetings") == 100
