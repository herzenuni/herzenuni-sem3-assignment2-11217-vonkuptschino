import sorts
import pytest
import hypothesis.strategies as st
from hypothesis import given


def test_param_b():
	lst = [2,1,2,8,5,0,6]
	assert sorts.bubble(lst) == sorted(lst)

def test_param_q():
	lst = [2,1,2,8,5,0,6]
	assert sorts.qsort(lst) == sorted(lst)

@given(st.lists(st.integers()))
def test_equal_bq(lst):
	assert sorts.bubble(lst) == sorts.qsort(lst)

@given(st.lists(st.integers()))
def test_equal_b(lst):
	assert sorts.bubble(lst) == sorted(lst)

@given(st.lists(st.integers()))
def test_equal_q(lst):
	assert sorts.qsort(lst) == sorted(lst)
