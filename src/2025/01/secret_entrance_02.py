""" AoC 2025 - Day 1 - Secret Entrance - Part 2 Module """
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


def same_sign(x: int, y: int) -> bool:
    """Return True if the sign of the two numbers is the same (zero counts as either)."""
    if x == 0 or y == 0:
        return True
    return x * y > 0


def get_password(data: list[int]) -> int:
    """Compute the password based on cumulative rotations."""
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
    """Run the Secret Entrance solver."""
    raw_data = read_file_in()
    data = prepare_data(raw_data)
    print(get_password(data))


if __name__ == "__main__":
    main()
