from pathlib import Path
from typing import List, Union

FILE_PATH = f"{Path(__file__).parent}/data.txt"

class Solution:

    def read_file_in(self) -> Union[List[int], List[int]]:
        left_column = []
        right_column = []

        with open(FILE_PATH, 'r', encoding="UTF-8") as file:
            for line in file:
                columns = line.split('   ')
                left_column.append(int(columns[0].strip()))
                right_column.append(int(columns[1].strip()))

        return left_column, right_column


    def measure_similarity(self, left_column: List[int], right_column: List[int]) -> int:
        left_column.sort()
        right_column.sort()

        total_similarity = 0

        for item in left_column:
            count = right_column.count(item)
            similarity = item * count
            if similarity > 0:
                total_similarity += similarity

        return total_similarity


def main():
    solution = Solution()
    left, right = solution.read_file_in()
    print(solution.measure_similarity(left, right))

if __name__ == "__main__":
    main()
