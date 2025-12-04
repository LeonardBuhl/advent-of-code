import re
from pathlib import Path

FILE_PATH = Path(__file__).with_name("data.txt")

def read_file_in() -> str:
    """ Read raw movement instructions from the local data file. """
    with open(FILE_PATH, "r", encoding="UTF-8") as file:
        contents = file.read()
    return contents


def format_data(data: str) -> list[list[str]]:
    formatted_data = [s.split('-') for s in data.split(',')]
    return formatted_data


def populate_ranges(data: list[list[str]]) -> list[str]:

    populated_data = []

    for x in data:
        start = int(x[0])
        populated_data.append(str(start))

        end = int(x[1])
        entry = start

        while entry < end:
            entry += 1
            populated_data.append(str(entry))

    return populated_data


def get_invalid_sum(data: list[str]) -> int:
    result = 0

    for num in data:

        if bool(re.fullmatch(r'(\d+)\1+', num)):
            result += int(num)

    return result


def main():
    data = read_file_in()
    data = format_data(data)
    data = populate_ranges(data)
    print(get_invalid_sum(data))


if __name__ == "__main__":
    main()
