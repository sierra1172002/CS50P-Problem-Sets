import pytest
from um import count




def test_count():

    assert count("Um, how are you doing?") == 1
    assert count("hello, um, world") == 1
    assert count("") == 0
    assert count("yummy") == 0
    assert count("What a bummer!") == 0
    assert count("Well, that was um, kind of funny :P") == 1