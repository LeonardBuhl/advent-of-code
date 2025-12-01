from pathlib import Path

FILE_PATH = f"{Path(__file__).parent}/data.txt"

class Solution:

    def read_file_in(self) -> list[int]:
        data = []

        with open(FILE_PATH, 'r', encoding="UTF-8") as file:
            for line in file:
                single_line_int = line.replace("L", "-")
                single_line_int = single_line_int.replace("R", "")
                data.append(int(single_line_int))

        return data


    def get_password(self, data: list[int]) -> int:
        
        current_pos = 50  # starting position
        point_at_zero = 0

        for rotation in data:

            current_pos = current_pos + rotation

            while current_pos >= 100:
                current_pos = current_pos - 100
            
            while current_pos <= -100:
                current_pos = current_pos + 100

            if current_pos == 0:
                point_at_zero += 1

        return point_at_zero


def main():
    sol = Solution()
    data = sol.read_file_in()
    print(sol.get_password(data))

if __name__ == "__main__":
    main()
