""" Tests for Mull It Over - Part 1 """
from mull_it_over_02 import get_result

DATA = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

def test_solution():
    assert get_result(DATA) == 48
