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
    assert get_solution(format_data(DATA)) == 43
