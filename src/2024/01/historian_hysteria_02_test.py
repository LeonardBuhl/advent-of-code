""" Tests for Historian Hysteria - Part 2 """
from historian_hysteria_02 import measure_similarity

left_column = [3, 4, 2, 1, 3, 3]
right_column = [4, 3, 5, 3, 9, 3]


def test_measure_similarity():
    """ Test the similarity measurement with sample data """
    assert measure_similarity(left_column, right_column) == 31
