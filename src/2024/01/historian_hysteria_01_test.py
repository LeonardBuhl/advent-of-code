""" Tests for Historian Hysteria - Part 1 """
from historian_hysteria_01 import measure_distance

left_column = [3, 4, 2, 1, 3, 3]
right_column = [4, 3, 5, 3, 9, 3]


def test_measure_distance():
    """ Test the distance measurement with the sample data """
    assert measure_distance(left_column, right_column) == 11
