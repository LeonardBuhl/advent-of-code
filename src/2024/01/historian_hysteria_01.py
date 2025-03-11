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


    def measure_distance(self, left_column: List[int], right_column: List[int]) -> int:
        left_column.sort()
        right_column.sort()

        total_distance = 0

        for id_left, item in enumerate(left_column):
            distance = item - right_column[id_left]
            if distance < 0:
                distance = distance * -1
            total_distance += distance

        return total_distance

def main():
    sol = Solution()
    left_column, right_column = sol.read_file_in()
    print(sol.total_distance(left_column, right_column))

if __name__ == "__main__":
    main()
