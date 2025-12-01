import pytest
from secret_entrance_01 import Solution

data = [
    "L68",
    "L30",
    "R48",
    "L5",
    "R60",
    "L55",
    "L1",
    "L99",
    "R14",
    "L82",
]

@pytest.fixture
def solution():
    return Solution()

def prepare_data():
    formatted_data = []
    for line in data:
        single_line_int = line.replace('L', '-')
        print(single_line_int)
        single_line_int = single_line_int.replace('R', '')
        formatted_data.append(int(single_line_int))
    return formatted_data

def test_solution(solution: Solution):
    formatted_data = prepare_data()
    assert solution.get_password(formatted_data) == 3
