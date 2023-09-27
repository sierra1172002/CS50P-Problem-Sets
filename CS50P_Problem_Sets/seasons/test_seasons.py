import pytest
from seasons import age_minutes

def test_correct():

    assert age_minutes(2000, 12, 12) == "Eleven million, nine hundred forty-one thousand, nine hundred twenty minutes"

def test_incorrect():

    assert age_minutes(2000, 31, 31) == "Invalid Date"