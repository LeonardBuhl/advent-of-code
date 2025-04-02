from pathlib import Path
from typing import List, Union

FILE_PATH = f"{Path(__file__).parent}/data.txt"

class Solution:

    def read_file_in(self) -> List[str]:

        dataset = []

        with open(FILE_PATH, 'r', encoding="UTF-8") as file:
            for line in file:
                dataset.append(line)

        return dataset


    def calculate_calibration_value(self, dataset: List[int]) -> int:

        calibration_sum = 0

        for line in dataset:
            numbers_list = []
            calibration_value = 0

            for index, character in enumerate(line):
                if character.isdigit():
                    numbers_list.append(character)

            if len(numbers_list) == 1:
                calibration_value = numbers_list[0] + numbers_list[0]
                calibration_value = int(calibration_value)

            elif len(numbers_list) >= 2:
                calibration_value = numbers_list[0] + numbers_list[-1]
                calibration_value = int(calibration_value)

            else:
                print(f"No Value found: {line=}")
                continue

            calibration_sum += calibration_value

        return calibration_sum


def main():
    sol = Solution()
    dataset = sol.read_file_in()
    print(sol.calculate_calibration_value(dataset))

if __name__ == "__main__":
    main()

