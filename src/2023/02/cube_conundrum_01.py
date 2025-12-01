from pathlib import Path
from typing import Dict, List

FILE_PATH = Path(__file__).with_name("data.txt")

# Structure:
# { id : { color : amount , color: amount ... } }

def read_file_in() -> List[str]:
    with open(FILE_PATH, "r", encoding="UTF-8") as file:
        return [line.rstrip("\n") for line in file]


def prepare_data(dataset: List[str]) -> Dict[int, Dict[str, int]]:
    def build_color_dict(color_list: List[str]) -> Dict[str, int]:
        color_dict: Dict[str, int] = {}
        color_dict["red"] = max([int(red.split()[0]) for red in color_list if "red" in red])
        color_dict["green"] = max([int(green.split()[0]) for green in color_list if "green" in green])
        color_dict["blue"] = max([int(blue.split()[0]) for blue in color_list if "blue" in blue])
        return color_dict

    structured_data: Dict[int, Dict[str, int]] = {}
    for line in dataset:
        key = int(line.split(":")[0].split()[1])
        temp_value = line.split(":")[1]
        temp_value = temp_value.split(";")
        value: List[str] = []
        for lst in temp_value:
            value.extend(lst.split(","))
        structured_data[key] = build_color_dict(color_list=value)

    return structured_data


def find_possible_games(structured_data: Dict[int, Dict[str, int]]) -> int:
    red, green, blue = 12, 13, 14
    id_sum = 0

    for key, value in structured_data.items():
        if value["red"] > red or value["green"] > green or value["blue"] > blue:
            continue
        id_sum += key

    return id_sum


def main() -> None:
    raw_data = read_file_in()
    structured_data = prepare_data(raw_data)
    print(f"{find_possible_games(structured_data)=}")


if __name__ == "__main__":
    main()
