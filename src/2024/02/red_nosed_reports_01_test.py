""" Tests for Red-Nosed Reports - Part 1 """
import red_nosed_reports_01

data = [
    [7, 6, 4, 2, 1],
    [1, 2, 7, 8, 9],
    [9, 7, 6, 2, 1],
    [1, 3, 2, 4, 5],
    [8, 6, 4, 4, 1],
    [1, 3, 6, 7, 9]
]


def test_solution():
    """ Test the safe report finding with the sample data """
    assert red_nosed_reports_01.find_safe_reports(data) == 2
