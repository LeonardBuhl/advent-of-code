""" AoC 2025 - Day 3 - Lobby - Part 1 Module """
from pathlib import Path

FILE_PATH = Path(__file__).with_name("data.txt")

def read_file_in() -> str:
    with open(FILE_PATH, "r", encoding="UTF-8") as file:
        contents = file.read()
    return contents


def format_data(data: str) -> list[list[int]]:
    lines = data.splitlines()
    formatted_data = [[int(char) for char in line] for line in lines]
    return formatted_data

def get_solution(data: list[list[int]]):
    result = 0

    for nums in data:

        first = second = 0

        # fast approach (first try)
        first = max(nums)
        f_index = nums.index(first)

        # index must be at least 2 smaller than len (1 for 0 base and 1 so there is a second number)
        if f_index <= len(nums) - 2:
            second = max(nums[f_index + 1 :])
            result += int(str(first) + str(second))
            continue

        # if that didn't worktry the slower approach
        first = second = 0
        f_index = -1
        for i, n in enumerate(nums):
            if n > first and i <= len(nums) - 2:
                first = n
                f_index = i
                second = 0
                continue

            if i > f_index and n > second:
                second = n
            
        result += int(str(first) + str(second))
    return result


def main():
    data = read_file_in()
    print(get_solution(format_data(data)))


if __name__ == "__main__":
    main()
