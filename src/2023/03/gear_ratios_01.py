from pathlib import Path
from typing import List

FILE_PATH = f"{Path(__file__).parent}/data.txt"
SYMBOLS = "@%#-/$&*+="


class Solution:

    def read_file_in(self) -> List[List[str]]:
        dataset = []

        with open(FILE_PATH, "r", encoding="UTF-8") as file:
            for line in file:
                dataset.append(list(line))

        return dataset

    def prepare_data(self, dataset: List[List[str]]) -> List[List[str]]:
        structured_data = []

        for outer_list in dataset:
            for inner_list in outer_list:
                structured_data.append(list(inner_list))

        return structured_data
                

    def find_symbols(self, structured_data) -> int:
        part_numbers = []
        for outer_index, inner_list in enumerate(structured_data):
            for inner_index, element in enumerate(inner_list):
                if element in SYMBOLS:
                    part_numbers.extend(self.get_adjacent_numbers_from_coords(structured_data, outer_index, inner_index))

        print(part_numbers)
        
        return sum(part_numbers)


    def get_adjacent_numbers_from_coords(self, dataset: List[List[str]], row: int, col: int) -> List[int]:
        """ returns a list of numbers that are adjacent to the current symbol """

        # prevent out of bounds errors:
        rows = len(dataset)
        cols = len(dataset[0]) if rows > 0 else 0
        part_numbers = []
        found_locations = []

        for i in range(max(0, row - 1), min(rows, row + 2)):
            for j in range(max(0, col - 1), min(cols, col + 2)):
                if (i, j) != (row, col) and (dataset[i][j]).isdigit():
                    if (i, j) not in found_locations:
                        # get the entire number
                        entire_number = [dataset[i][j]]
                        found_locations.append((i, j))
                        
                        # go left
                        left = j - 1
                        while left >= 0 and (dataset[i][left]).isdigit():
                                entire_number.insert(0, dataset[i][left])
                                found_locations.append((i, left))
                                left -= 1

                        # go right
                        right = j + 1
                        while right <= len(dataset[i]) and (dataset[i][right]).isdigit():
                            entire_number.append(dataset[i][right])
                            found_locations.append((i, right))
                            right += 1

                        # entire number found, combine into integer
                        part_numbers.append(int(''.join(map(str, entire_number))))
                    
        return part_numbers



def main():
    solution = Solution()
    raw_data = solution.read_file_in()
    structured_data = solution.prepare_data(raw_data)
    print(f"{solution.find_symbols(structured_data)=}")


if __name__ == "__main__":
    main()
