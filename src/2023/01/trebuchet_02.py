""" AoC 2023 - Day 1 - Trebuchet Calibration - Part 2 """
import re
from pathlib import Path
from typing import Dict, List

FILE_PATH = Path(__file__).with_name("data.txt")


def read_file_in(file_path: Path = FILE_PATH) -> List[str]:
    dataset: List[str] = []
    with open(file_path, "r", encoding="UTF-8") as file:
        for line in file:
            dataset.append(line)
    return dataset


NUMBER_STRINGS: Dict[str, str] = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

PATTERN = re.compile("|".join(re.escape(s) for s in NUMBER_STRINGS))


def prepare_string(line: str) -> str:
    result = ""
    i = 0

    while i < len(line):
        match = PATTERN.search(line, i)
        if match:
            result += line[i : match.start()] + NUMBER_STRINGS[match.group(0)]
            i = match.start() + 1
        else:
            result += line[i:]
            break

    return result


def calculate_calibration_value(dataset: List[str]) -> int:
    calibration_sum = 0

    for original_line in dataset:
        line = prepare_string(original_line)
        numbers_list: List[str] = [c for c in line if c.isdigit()]

        if len(numbers_list) == 1:
            calibration_value = int(numbers_list[0] * 2)
        elif len(numbers_list) >= 2:
            calibration_value = int(numbers_list[0] + numbers_list[-1])
        else:
            print(f"No Value found: {original_line=}")
            continue

        calibration_sum += calibration_value

    return calibration_sum


def main() -> None:
    dataset = read_file_in()
    print(calculate_calibration_value(dataset))


if __name__ == "__main__":
    main()
