import pytest

@pytest.mark.parametrize(
    "a,b,expected",
    [(1,5,5),(2,5,10),(0,0,0),(-1,-4,4),(2,-3,-6)]
)
def test_multiplication(a,b,expected):
    assert a*b == expected