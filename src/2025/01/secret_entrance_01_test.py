""" Tests for Secret Entrance - Part 1 """
from secret_entrance_01 import format_data, get_solution

DATA = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""


def test_solution():
    """ test the solution with the provided example """
    assert get_solution(format_data(DATA)) == 3
