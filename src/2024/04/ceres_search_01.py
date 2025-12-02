from pathlib import Path
from typing import List

FILE_PATH = Path(__file__).with_name("data.txt")

def read_file_in() -> str:
    """ Read raw movement instructions from the local data file. """
    with open(FILE_PATH, "r", encoding="UTF-8") as file:
        contents = file.read()
    return contents


def format_data(data: str) -> List[List[str]]:
    lines = data.splitlines()
    formatted_data = [[char for char in line] for line in lines]
    return formatted_data


def solve_word_search(data: List[List[str]]) -> int: 
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

    

    return result


def main():
    data = read_file_in()
    data = format_data(data)
    print(solve_word_search(data))


if __name__ == "__main__":
    main()