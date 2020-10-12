import pytest
def test_addition():
    assert 1+1 == 2

def test_substraction():
    diff = 2-2
    assert diff == 0

def test_devideByZero():
    with pytest.raises(ZeroDivisionError):
        1/0