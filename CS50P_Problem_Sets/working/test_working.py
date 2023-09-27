import pytest
from working import convert



def test_correct():

    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("12 PM to 3 PM") == "12:00 to 15:00"
    assert convert("12 AM to 4 PM") == "00:00 to 16:00"
    assert convert("9:30 AM to 5:30 PM") == "09:30 to 17:30"

def test_incorrect():

    with pytest.raises(ValueError):
        convert("12:60 PM to 1:30 PM")
    with pytest.raises(ValueError):
        convert("12:00 AM to 15:00 PM")
    with pytest.raises(ValueError):
        convert("12:00 to 15:00")
    with pytest.raises(ValueError):
        convert(" to 15:00")
    with pytest.raises(ValueError):
        convert("cat")
