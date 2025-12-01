from pathlib import Path
from typing import List

FILE_PATH = Path(__file__).with_name("data.txt")

def read_file_in() -> tuple[list[int], list[int]]:
    data = []

    with open(FILE_PATH, 'r', encoding="UTF-8") as file:
        for line in file:
            single_line_string = line.split()
            single_line_int = [int(number) for number in single_line_string]
            data.append(single_line_int)

    return data

def is_valid_ascending(numbers: List[int]) -> bool:
    return all(0 < b - a <= 3 for a, b in zip(numbers, numbers[1:]))

def is_valid_descending(numbers: List[int]) -> bool:
    return all(0 < a - b <= 3 for a, b in zip(numbers, numbers[1:]))


def find_safe_reports(data: List[List[int]]) -> int:

    number_safe_reports = 0

    for report in data:

        if is_valid_ascending(report) or is_valid_descending(report):
            number_safe_reports += 1


    return number_safe_reports


def main():
    data = read_file_in()
    print(find_safe_reports(data))

if __name__ == "__main__":
    main()
