import pytest
from historian_hysteria_01 import Solution

left_column = [3, 4, 2, 1, 3, 3]
right_column = [4, 3, 5, 3, 9, 3]


@pytest.fixture
def solution():
    return Solution()

def test_solution(solution: Solution):
    assert solution.measure_distance(left_column, right_column) == 11
