import pytest
from trebuchet_01 import Solution

dataset = [
    "1abc2",
    "pqr3stu8vwx",
    "a1b2c3d4e5f",
    "treb7uchet"
]

@pytest.fixture
def solution():
    return Solution()

def test_solution(sol: Solution):
    assert sol.calculate_calibration_value([dataset[0]]) == 12
    assert sol.calculate_calibration_value([dataset[1]]) == 38
    assert sol.calculate_calibration_value([dataset[2]]) == 15
    assert sol.calculate_calibration_value([dataset[3]]) == 77
    assert sol.calculate_calibration_value(dataset) == 142
