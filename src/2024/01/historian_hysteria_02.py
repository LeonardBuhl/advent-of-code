""" AoC 2024 - Day 1 - Historian Hysteria - Part 2 Module """
from pathlib import Path
from typing import List, Tuple

FILE_PATH = Path(__file__).with_name("data.txt")


def read_file_in() -> str:
    with open(FILE_PATH, "r", encoding="UTF-8") as file:
        contents = file.read()
    return contents


def format_data(data: str) -> Tuple[List[int], List[int]]:
    """ split the puzzle input into two integer lists """
    left_column: List[int] = []
    right_column: List[int] = []

    lines = data.splitlines()
    for line in lines:
        columns = line.strip().split()
        left_column.append(int(columns[0].strip()))
        right_column.append(int(columns[1].strip()))

    return left_column, right_column


def get_solution(left_column: List[int], right_column: List[int]) -> int:
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
    left, right = format_data(read_file_in())
    print(get_solution(left, right))


if __name__ == "__main__":
    main()
