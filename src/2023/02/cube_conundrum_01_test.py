import pytest
from cube_conundrum_01 import find_possible_games, prepare_data

dataset = [
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
]


@pytest.mark.parametrize(
    ("line", "expected"),
    [
        ([dataset[0]], 1),
        ([dataset[1]], 2),
        ([dataset[2]], 0),
        ([dataset[3]], 0),
        ([dataset[4]], 5),
        (dataset, 8),
    ],
)
def test_solution(line, expected):
    assert find_possible_games(prepare_data(line)) == expected
