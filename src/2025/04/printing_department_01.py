""" AoC 2025 - Day 4 - Printing Department - Part 1 Module """
from pathlib import Path

FILE_PATH = Path(__file__).with_name("data.txt")

DIRECTIONS = [
        (-1, -1), # Top-left
        (-1, 0),  # Up
        (-1, 1),  # Top-right
        (0, 1),   # Right
        (1, 1),   # Bottom-right
        (1, 0),   # Down
        (1, -1),  # Bottom-left
        (0, -1),  # Left
    ]

def read_file_in() -> str:
    with open(FILE_PATH, "r", encoding="UTF-8") as file:
        contents = file.read()
    return contents


def format_data(data: str) -> list[list[str]]:
    lines = data.splitlines()
    formatted_data = [list(line) for line in lines]
    return formatted_data


def get_solution(data) -> int:
    result = 0
    max_rolls = 3

    indices = []

    for y, row in enumerate(data):

        for x, elem in enumerate(row):
        
            if elem == '.':
                continue

            if elem == '@':
                rolls = 0
                for dx, dy in DIRECTIONS:

                    # ensure only valid indices are checked
                    if 0 <= x + dx < len(row) and 0 <= y + dy < len(data):
                        if data[y + dy][x + dx] == '@':
                            rolls += 1
                    # x + dx and y + dy need to stay within the bounds of the 2d array
                    # 0 <= x + dx and x + dx < len(row)
                    # 0 <= y + dy and y + dy <= len(data)


                if rolls <= max_rolls:
                    result += 1
                    indices.append((x, y))

    return result


def main():
    data = read_file_in()
    print(get_solution(format_data(data)))


if __name__ == "__main__":
    main()
