import re
from pathlib import Path

FILE_PATH = Path(__file__).with_name("data.txt")

def read_file_in() -> str:
    """ Read raw movement instructions from the local data file. """
    with open(FILE_PATH, "r", encoding="UTF-8") as file:
        contents = file.read()
    return contents


def get_result(data: str):
    result = 0

    mul_pattern = r'mul\(\d{1,3},\d{1,3}\)'
    matches = re.findall(mul_pattern, data)

    for mul in matches:
        digit_pattern = r'\d+'
        numbers = re.findall(digit_pattern, mul)
        result += int(numbers[0]) * int(numbers[1])

    return result


def main():
    data = read_file_in()
    print(get_result(data))


if __name__ == "__main__":
    main()
