from pathlib import Path
from typing import List, Dict


FILE_PATH = f"{Path(__file__).parent}/data.txt"

# Structure:
# { id : { color : amount , color: amount ... } }


class Solution:
    def read_file_in(self) -> List[str]:
        dataset = []

        with open(FILE_PATH, "r", encoding="UTF-8") as file:
            for line in file:
                dataset.append(line)

        return dataset

    def prepare_data(self, dataset: List[str]) -> Dict[int, Dict[str, int]]:
        def build_color_dict(color_list: List[str]) -> Dict[str, int]:
            color_dict = {}

            color_dict["red"] = max(
                [int(red.split()[0]) for red in color_list if "red" in red]
            )
            color_dict["green"] = max(
                [int(green.split()[0]) for green in color_list if "green" in green]
            )
            color_dict["blue"] = max(
                [int(blue.split()[0]) for blue in color_list if "blue" in blue]
            )

            return color_dict

        structured_data = {}

        for line in dataset:
            key = line.split(":")[0].split()[1]
            temp_value = line.split(":")[1]
            temp_value = temp_value.split(";")
            value = []
            for lst in temp_value:
                value.extend(lst.split(","))
            structured_data[key] = build_color_dict(color_list=value)

        return structured_data

    def find_possible_games(self, structured_data: Dict[int, Dict[str, int]]) -> int:
        set_power = 0
        result = 0

        for key, value in structured_data.items():
            set_power = value["red"] * value["green"] * value["blue"]
            result += set_power

        return result


def main():
    solution = Solution()
    raw_data = solution.read_file_in()
    structured_data = solution.prepare_data(raw_data)
    print(f"{solution.find_possible_games(structured_data)=}")


if __name__ == "__main__":
    main()
