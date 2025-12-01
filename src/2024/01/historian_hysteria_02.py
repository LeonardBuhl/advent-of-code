""" AoC 2024 - Day 1 - Historian Hysteria - Part 2 Module """
from pathlib import Path
from typing import List, Tuple

FILE_PATH = Path(__file__).with_name("data.txt")


def read_file_in() -> Tuple[List[int], List[int]]:
    """ Read two integer columns from the puzzle input file. """
    left_column: List[int] = []
    right_column: List[int] = []

    with open(FILE_PATH, "r", encoding="UTF-8") as file:
        for line in file:
            columns = line.split("   ")
            left_column.append(int(columns[0].strip()))
            right_column.append(int(columns[1].strip()))

    return left_column, right_column


def measure_similarity(left_column: List[int], right_column: List[int]) -> int:
    """ Compute the similarity score by counting matching values. """
    left_column.sort()
    right_column.sort()

    total_similarity = 0

    for item in left_column:
        count = right_column.count(item)
        similarity = item * count
        if similarity > 0:
            total_similarity += similarity

    return total_similarity


def main() -> None:
    """ Entry point for running the similarity calculator. """
    left, right = read_file_in()
    print(measure_similarity(left, right))


if __name__ == "__main__":
    main()
