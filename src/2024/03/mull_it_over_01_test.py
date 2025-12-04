""" Tests for Mull It Over - Part 1 """
from mull_it_over_01 import get_solution

DATA = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"


def test_solution():
    """ Test the solution function """
    assert get_solution(DATA) == 161
