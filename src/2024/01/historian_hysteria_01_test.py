""" Tests for Historian Hysteria - Part 1 """
from historian_hysteria_01 import get_solution, format_data

DATA = \
"""3   4
4   3
2   5
1   3
3   9
3   3"""

def test_solution():
    """ Test the distance measurement with the sample data """
    left_column, right_column = format_data(DATA)
    assert get_solution(left_column, right_column) == 11
