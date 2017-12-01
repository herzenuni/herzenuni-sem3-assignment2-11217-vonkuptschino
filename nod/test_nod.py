from nod import *
import pytest
import hypothesis.strategies as st
from hypothesis import given

@pytest.mark.parametrize("a, b, result", [
  											(18,30,6),
  											(10,20,10),
  											(0,0,0)])
def test_gcd(a, b, result):
    assert(gcd(a, b) == result)

@given(st.integers(), st.integers())
def test_hypogcd(x, y):
    if(gcd(x,y) != 0):
        assert((x % gcd(x,y) == 0) and (y % gcd(x,y) == 0))