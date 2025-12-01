import pytest
from gear_ratios_01 import Solution

dataset = [
    ["467..114.."],
    ["...*......"],
    ["..35..633."],
    ["......#..."],
    ["617*......"],
    [".....+.58."],
    ["..592....."],
    ["......755."],
    ["...$.*...."],
    [".664.598.."],
]

@pytest.fixture
def solution() -> Solution:
    return Solution()

def test_solution(solution: Solution):
    assert solution.find_symbols(solution.prepare_data(dataset)) == 4361
