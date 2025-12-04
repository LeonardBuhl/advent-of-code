""" AoC 2025 - Day 3 - Lobby - Part 2 Module """
from pathlib import Path

FILE_PATH = Path(__file__).with_name("data.txt")


def read_file_in() -> str:
    """ Read the input file """
    with open(FILE_PATH, "r", encoding="UTF-8") as file:
        contents = file.read()
    return contents


def format_data(data: str) -> list[list[int]]:
    """ Format the input data into a 2D list """
    lines = data.splitlines()
    formatted_data = [[int(char) for char in line] for line in lines]
    return formatted_data


def get_solution(data: list[list[int]]) -> int:
    """ Get the solution for the challenge """
    result = 0
    target_length = 12

    for nums in data:

        to_drop = len(nums) - target_length
        stack = []

        for num in nums:
            while to_drop > 0 and stack and stack[-1] < num:
                stack.pop()
                to_drop -= 1
            stack.append(num)

        best = stack[:target_length]
        result += int("".join(map(str, best)))

    return result


def main():
    """ main """
    data = read_file_in()
    print(get_solution(format_data(data)))


if __name__ == "__main__":
    main()
