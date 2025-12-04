""" Test for Printing Department - Part 1 """
from printing_department_01 import get_solution, format_data


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
    assert get_solution(format_data(DATA)) == 13
