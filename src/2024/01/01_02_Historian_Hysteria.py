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

total_similarity = 0

for item in left_column:
    count = right_column.count(item)
    similarity = item * count
    if similarity > 0:
        total_similarity += similarity

print(total_similarity)
