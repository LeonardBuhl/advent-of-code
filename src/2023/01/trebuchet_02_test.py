import pytest
from trebuchet_02 import Solution

dataset = [
    "two1nine",
    "eighttwothree",
    "abcone2threexyz",
    "xtwone3four",
    "4nineeightseven2",
    "zoneight234",
    "7pqrstsixteen",
]

@pytest.fixture
def solution():
    return Solution()

def test_solution(sol: Solution):
    assert sol.calculate_calibration_value([dataset[0]]) == 29
    assert sol.calculate_calibration_value([dataset[1]]) == 83
    assert sol.calculate_calibration_value([dataset[2]]) == 13
    assert sol.calculate_calibration_value([dataset[3]]) == 24
    assert sol.calculate_calibration_value([dataset[4]]) == 42
    assert sol.calculate_calibration_value([dataset[5]]) == 14
    assert sol.calculate_calibration_value([dataset[6]]) == 76
    assert sol.calculate_calibration_value(dataset) == 281
