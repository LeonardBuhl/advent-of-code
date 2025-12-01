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
    
    def same_sign(self, x: int, y: int) -> bool:
        """ returns true if the sign of the two given numbers is the same. False if they are different """
        if x == 0 or y == 0:
            return True
        return x * y > 0


    def get_password(self, data: list[int]) -> int:
        
        current_pos = 50  # starting position
        point_at_zero = 0

        prev = current_pos

        for rotation in data:

            current_pos = current_pos + rotation

            if not self.same_sign(current_pos, prev):
                point_at_zero += 1

            while current_pos >= 100:
                current_pos = current_pos - 100
                if current_pos != 0:
                    point_at_zero += 1
            
            while current_pos <= -100:
                current_pos = current_pos + 100
                if current_pos != 0:
                    point_at_zero += 1

            if current_pos == 0:
                point_at_zero += 1

            prev = current_pos

        return point_at_zero


def main():
    solution = Solution()
    data = solution.read_file_in()
    print(solution.get_password(data))

if __name__ == "__main__":
    main()
