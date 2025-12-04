""" Test for Lobby - Part 2 """
from lobby_02 import get_solution, format_data


DATA = """987654321111111
811111111111119
234234234234278
818181911112111
"""

def test_solution():
    """ test the solution with the provided example """
    assert get_solution(format_data(DATA)) == 3121910778619
