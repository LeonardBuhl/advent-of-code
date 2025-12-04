""" AoC 2024 - Day 4 - Ceres Search - Part 1 Module """
from pathlib import Path
from typing import List

FILE_PATH = Path(__file__).with_name("data.txt")


def read_file_in() -> str:
    """ Read raw movement instructions from the local data file. """
    with open(FILE_PATH, "r", encoding="UTF-8") as file:
        contents = file.read()
    return contents


def format_data(data: str) -> List[List[str]]:
    """ Format the input data into a 2D list """
    lines = data.splitlines()
    formatted_data = [list(line) for line in lines]
    return formatted_data


def get_solution(data: List[List[str]]) -> int:
    """ Get the solution for the challenge """
    result = 0

    max_x = len(data[0])
    max_y = len(data)

    target = ['XMAS', 'SAMX']

    # horizontal
    for row in data:
        for x in range(max_x - 3):
            result += ''.join(row[x:x + 4]) in target

    # vertical
    for column in zip(*data):
        for y in range(max_y - 3):
            result += ''.join(column[y:y + 4]) in target

    # diagonal
    for row in range(max_y - 3):
        for col in range(max_x - 3):
            top_left_to_bottom_right = ''.join([
                data[row][col],
                data[row+1][col+1],
                data[row+2][col+2],
                data[row+3][col+3]
            ])
            bottom_left_to_top_right = ''.join([
                data[row+3][col],
                data[row+2][col+1],
                data[row+1][col+2],
                data[row][col+3]
            ])
            result += top_left_to_bottom_right in target
            result += bottom_left_to_top_right in target

    return result


def main():
    """ main """
    data = read_file_in()
    print(get_solution(format_data(data)))


if __name__ == "__main__":
    main()
