""" AoC 2025 - Day 1 - Secret Entrance - Part 2 Module """
from pathlib import Path

FILE_PATH = Path(__file__).with_name("data.txt")


def read_file_in() -> str:
    """ Read raw movement instructions from the local data file. """
    with open(FILE_PATH, "r", encoding="UTF-8") as file:
        contents = file.read()
    return contents


def format_data(data: str) -> list[int]:
    """ Convert L/R instructions into signed integer rotations. """
    formatted = []

    lines = data.splitlines()
    for line in lines:
        line = line.strip()
        single_line_int = line.replace("L", "-").replace("R", "")
        formatted.append(int(single_line_int))

    return formatted


def same_sign(x: int, y: int) -> bool:
    """ Return True if the sign of the two numbers is the same (zero counts as either). """
    if x == 0 or y == 0:
        return True
    return x * y > 0


def get_solution(data: list[int]) -> int:
    """ Compute the password based on cumulative rotations. """
    current_pos = 50  # starting position
    point_at_zero = 0
    prev = current_pos

    for rotation in data:
        current_pos += rotation

        if not same_sign(current_pos, prev):
            point_at_zero += 1

        while current_pos >= 100:
            current_pos -= 100
            if current_pos != 0:
                point_at_zero += 1

        while current_pos <= -100:
            current_pos += 100
            if current_pos != 0:
                point_at_zero += 1

        if current_pos == 0:
            point_at_zero += 1

        prev = current_pos

    return point_at_zero


def main() -> None:
    """ Run the Secret Entrance solver. """
    data = read_file_in()
    print(get_solution(format_data(data)))


if __name__ == "__main__":
    main()
