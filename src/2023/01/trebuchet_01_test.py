""" AoC 2023 - Day 1 - Trebuchet Calibration - Tests for Part 1 """
import pytest
from trebuchet_01 import calculate_calibration_value

dataset = [
    "1abc2",
    "pqr3stu8vwx",
    "a1b2c3d4e5f",
    "treb7uchet",
]


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        ([dataset[0]], 12),
        ([dataset[1]], 38),
        ([dataset[2]], 15),
        ([dataset[3]], 77),
        (dataset, 142),
    ],
)
def test_calculate_calibration_value(lines, expected):
    assert calculate_calibration_value(lines) == expected
