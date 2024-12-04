from pathlib import Path

left_column = []
right_column = []

FILE_PATH = f"{Path(__file__).parent}\\data.txt"
with open(FILE_PATH, 'r', encoding="UTF-8") as file:
    for line in file:
        columns = line.split('   ')
        left_column.append(int(columns[0].strip()))
        right_column.append(int(columns[1].strip()))

left_column.sort()
right_column.sort()

total_distance = 0

for id_left, item in enumerate(left_column):
    distance = item - right_column[id_left]
    if distance < 0:
        distance = distance * -1
    total_distance += distance

print(total_distance)
