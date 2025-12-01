""" AoC 2023 - Day 1 - Trebuchet Calibration - Part 1 """
from pathlib import Path
from typing import List

FILE_PATH = Path(__file__).with_name("data.txt")

def read_file_in(file_path: Path = FILE_PATH) -> List[str]:
    dataset: List[str] = []
    with open(file_path, "r", encoding="UTF-8") as file:
        for line in file:
            dataset.append(line)
    return dataset


def calculate_calibration_value(dataset: List[str]) -> int:
    calibration_sum = 0

    for line in dataset:
        numbers_list: List[str] = []

        for character in line:
            if character.isdigit():
                numbers_list.append(character)

        if len(numbers_list) == 1:
            calibration_value = int(numbers_list[0] * 2)
        elif len(numbers_list) >= 2:
            calibration_value = int(numbers_list[0] + numbers_list[-1])
        else:
            print(f"No Value found: {line=}")
            continue

        calibration_sum += calibration_value

    return calibration_sum


def main() -> None:
    dataset = read_file_in()
    print(calculate_calibration_value(dataset))


if __name__ == "__main__":
    main()
