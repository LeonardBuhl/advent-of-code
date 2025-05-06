from pathlib import Path

FILE_PATH = f"{Path(__file__).parent}/data.txt"

symbols = []

with open(FILE_PATH, "r", encoding="UTF-8") as file:
    for line in file:
        for char in line:
            if not char.isdigit() and char != "." and char != "\n":
                symbols.append(char)

symbols = set(symbols)
print(''.join(symbols))

