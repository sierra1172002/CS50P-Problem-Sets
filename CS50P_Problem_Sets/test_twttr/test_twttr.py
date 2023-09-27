from twttr import shorten


def test_lower():
    assert shorten("my first tweet") == "my frst twt"


def test_upper():
    assert shorten("MY FIRST TWEET") == "MY FRST TWT"



def test_all_vowels():
    assert shorten("aeiou") == ""


def test_punctuation():

    assert shorten("Voila!") == "Vl!"


def test_numbers():
    assert shorten("This is CS50") == "Ths s CS50"
