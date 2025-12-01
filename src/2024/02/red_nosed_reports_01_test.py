import pytest
from red_nosed_reports_01 import Solution

data = [
    [7, 6, 4, 2, 1],
    [1, 2, 7, 8, 9],
    [9, 7, 6, 2, 1],
    [1, 3, 2, 4, 5],
    [8, 6, 4, 4, 1],
    [1, 3, 6, 7, 9]
]

@pytest.fixture
def solution():
    return Solution()

def test_solution(solution: Solution):
    assert solution.find_safe_reports(data) == 2
