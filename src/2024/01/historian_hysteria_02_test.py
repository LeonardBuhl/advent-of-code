import pytest
from historian_hysteria_02 import Solution

left_column = [3, 4, 2, 1, 3, 3]
right_column = [4, 3, 5, 3, 9, 3]

@pytest.fixture
def solution():
    return Solution()

def test_solution(sol: Solution):
    assert sol.measure_similarity(left_column, right_column) == 31
