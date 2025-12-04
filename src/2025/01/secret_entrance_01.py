""" AoC 2025 - Day 1 - Secret Entrance - Part 1 Module """
from pathlib import Path

FILE_PATH = Path(__file__).with_name("data.txt")

def read_file_in() -> list[str]:
    """ Read raw movement instructions from the local data file. """
    with open(FILE_PATH, "r", encoding="UTF-8") as file:
        return [line.strip() for line in file]

def prepare_data(raw_data: list[str]) -> list[int]:
    """Convert L/R instructions into signed integer rotations."""
    formatted = []
    for line in raw_data:
        single_line_int = line.replace("L", "-").replace("R", "")
        formatted.append(int(single_line_int))
    return formatted

def get_solution(data: list[int]) -> int:
    """ Count how often the position returns to zero when applying rotations. """
    current_pos = 50
    point_at_zero = 0
    for rotation in data:
        current_pos += rotation
        while current_pos >= 100:
            current_pos -= 100
        while current_pos <= -100:
            current_pos += 100
        if current_pos == 0:
            point_at_zero += 1
    return point_at_zero

def main():
    """ Entry point for running the password calculation. """
    data = read_file_in()
    print(get_solution(prepare_data(data)))

if __name__ == "__main__":
    main()
