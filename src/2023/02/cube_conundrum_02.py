from pathlib import Path
from typing import Dict, List

FILE_PATH = Path(__file__).with_name("data.txt")


def read_file_in() -> List[str]:
    dataset = []
    with open(FILE_PATH, "r", encoding="UTF-8") as file:
        for line in file:
            dataset.append(line)
    return dataset


def prepare_data(dataset: List[str]) -> Dict[str, Dict[str, int]]:
    def build_color_dict(color_list: List[str]) -> Dict[str, int]:
        color_dict = {}
        color_dict["red"] = max(
            (int(red.split()[0]) for red in color_list if "red" in red), default=0
        )
        color_dict["green"] = max(
            (int(green.split()[0]) for green in color_list if "green" in green),
            default=0,
        )
        color_dict["blue"] = max(
            (int(blue.split()[0]) for blue in color_list if "blue" in blue), default=0
        )
        return color_dict

    structured_data: Dict[str, Dict[str, int]] = {}
    for line in dataset:
        key = line.split(":")[0].split()[1]
        temp_value = line.split(":")[1]
        temp_value = temp_value.split(";")
        value: List[str] = []
        for lst in temp_value:
            value.extend(lst.split(","))
        structured_data[key] = build_color_dict(color_list=value)

    return structured_data


def find_possible_games(structured_data: Dict[str, Dict[str, int]]) -> int:
    set_power = 0
    result = 0
    for value in structured_data.values():
        set_power = value["red"] * value["green"] * value["blue"]
        result += set_power
    return result


def main() -> None:
    raw_data = read_file_in()
    structured_data = prepare_data(raw_data)
    print(f"{find_possible_games(structured_data)=}")


if __name__ == "__main__":
    main()
