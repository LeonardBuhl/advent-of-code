""" Test for Printing Department - Part 2 """
from printing_department_02 import get_solution, format_data


DATA = \
"""..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""

def test_solution():
    """ test the solution with the provided example """
    assert get_solution(format_data(DATA)) == 43
