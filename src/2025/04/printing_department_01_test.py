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
    assert get_solution(format_data(DATA)) == 13
