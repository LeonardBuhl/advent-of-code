from pathlib import Path

data = []

FILE_PATH = f"{Path(__file__).parent}\\data.txt"
with open(FILE_PATH, 'r', encoding="UTF-8") as file:
    for line in file:
        single_line_string = line.split()
        single_line_int = [int(number) for number in single_line_string]
        data.append(single_line_int)

number_safe_reports = 0

for array in data:

    direction = "unset"
    print(array)

    for id_number, number in enumerate(array):

        if id_number == len(array) - 1: # avoid IndexError
            number_safe_reports += 1 # if last number, it's safe
            direction = "unset"
            break

        level_difference = array[id_number + 1] - number

        if direction == "unset":
            if level_difference > 0:
                direction = "+"
            elif level_difference < 0:
                direction = "-"

        if direction == "+":
            if level_difference <= 0 or level_difference > 3:
                break

        if direction == "-":
            if level_difference >= 0 or level_difference < -3:
                break

print(number_safe_reports)