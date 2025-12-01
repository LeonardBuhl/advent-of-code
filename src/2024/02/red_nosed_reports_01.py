from pathlib import Path
from typing import List

FILE_PATH = f"{Path(__file__).parent}/data.txt"

class Solution:

    def read_file_in(self) -> List[List[int]]:
        data = []

        with open(FILE_PATH, 'r', encoding="UTF-8") as file:
            for line in file:
                single_line_string = line.split()
                single_line_int = [int(number) for number in single_line_string]
                data.append(single_line_int)

        return data


    def find_safe_reports(self, data: List[List[int]]) -> int:

        number_safe_reports = 0

        for array in data:

            direction = "unset"
            string = "unsafe"

            for id_number, number in enumerate(array):

                if id_number == len(array) - 1: # avoid IndexError
                    number_safe_reports += 1 # if last number, it's safe
                    direction = "unset"
                    string = "safe"
                    break

                level_difference = array[id_number + 1] - number

                # i still don´t know exactly why but the other checks dont catch 5 cases that this catches
                a = abs(level_difference)
                if a == 0 or a > 3:
                    break

                if direction == "unset":
                    if level_difference > 0:
                        direction = "+"
                    elif level_difference < 0:
                        direction = "-"

                # direction is increasing
                if direction == "+":
                    # decreasing again or increasing by more than three
                    if level_difference <= 0 or level_difference > 3:
                        break

                if direction == "-":
                    if level_difference >= 0 or level_difference < -3:
                        break

            print(f"{array} - {string}")

        return number_safe_reports


def main():
    sol = Solution()
    data = sol.read_file_in()
    print(sol.find_safe_reports(data))

if __name__ == "__main__":
    main()
