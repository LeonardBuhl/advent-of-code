""" Test for Ceres Search - Part 1 """
from ceres_search_01 import get_solution, format_data

DATA = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""


def test_solution():
    """ test the solution with the provided example """
    assert get_solution(format_data(DATA)) == 18
