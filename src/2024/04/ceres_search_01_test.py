from ceres_search_01 import solve_word_search, format_data

DATA = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""

def test_solution():
    assert solve_word_search(format_data(DATA)) == 18
