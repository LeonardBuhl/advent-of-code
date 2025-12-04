""" AoC 2024 - Day 2 - Red-Nosed Reports - Part 2 Module """
from pathlib import Path
from typing import List

FILE_PATH = Path(__file__).with_name("data.txt")


def read_file_in() -> str:
    """ Read raw movement instructions from the local data file. """
    with open(FILE_PATH, "r", encoding="UTF-8") as file:
        contents = file.read()
    return contents


def format_data(data: str) -> List[List[int]]:
    lines = data.splitlines()
    lines = [line.split() for line in lines]
    formatted_data = [[int(n) for n in line] for line in lines]
    return formatted_data


def is_valid_ascending(numbers: List[int]) -> bool:
    return all(0 < b - a <= 3 for a, b in zip(numbers, numbers[1:]))


def is_valid_descending(numbers: List[int]) -> bool:
    return all(0 < a - b <= 3 for a, b in zip(numbers, numbers[1:]))


def get_solution(data: List[List[int]]) -> int:

    number_safe_reports = 0

    for report in data:

        report_variations = [report[:i] + report[i+1:]
                             for i in range(len(report))]

        for report_variant in report_variations:

            if is_valid_ascending(report_variant) or is_valid_descending(report_variant):
                number_safe_reports += 1
                break

    return number_safe_reports


def main():
    data = read_file_in()
    print(get_solution(format_data(data)))


if __name__ == "__main__":
    main()
