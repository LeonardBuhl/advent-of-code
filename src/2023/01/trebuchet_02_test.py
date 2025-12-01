""" AoC 2023 - Day 1 - Trebuchet Calibration - Part 2 """
import pytest
from trebuchet_02 import calculate_calibration_value

dataset = [
    "two1nine",
    "eighttwothree",
    "abcone2threexyz",
    "xtwone3four",
    "4nineeightseven2",
    "zoneight234",
    "7pqrstsixteen",
]


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        ([dataset[0]], 29),
        ([dataset[1]], 83),
        ([dataset[2]], 13),
        ([dataset[3]], 24),
        ([dataset[4]], 42),
        ([dataset[5]], 14),
        ([dataset[6]], 76),
        (dataset, 281),
    ],
)
def test_calculate_calibration_value(lines, expected):
    assert calculate_calibration_value(lines) == expected
