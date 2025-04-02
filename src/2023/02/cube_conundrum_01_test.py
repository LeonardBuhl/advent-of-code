import pytest
from cube_conundrum_01 import Solution

dataset = []

@pytest.fixture
def solution():
    return Solution()

def test_solution(solution: Solution):
    assert solution.pass == 0
