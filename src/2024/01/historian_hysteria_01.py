""" AoC 2024 - Day 1 - Historian Hysteria - Part 1 Module """
from pathlib import Path
from typing import List, Tuple

FILE_PATH = Path(__file__).with_name("data.txt")


def read_file_in() -> Tuple[List[int], List[int]]:
    """ Load and split the puzzle input into two integer lists. """
    left_column: List[int] = []
    right_column: List[int] = []

    with open(FILE_PATH, "r", encoding="UTF-8") as file:
        for line in file:
            columns = line.strip().split()
            left_column.append(int(columns[0].strip()))
            right_column.append(int(columns[1].strip()))

    return left_column, right_column


def measure_distance(left_column: List[int], right_column: List[int]) -> int:
    """ Return the sum of absolute differences between the sorted columns. """
    left_sorted = sorted(left_column)
    right_sorted = sorted(right_column)

    total_distance = 0
    for idx, value in enumerate(left_sorted):
        distance = abs(value - right_sorted[idx])
        total_distance += distance

    return total_distance


def main() -> None:
    """ Print the total distance between the two columns. """
    left_column, right_column = read_file_in()
    print(measure_distance(left_column, right_column))


if __name__ == "__main__":
    main()
