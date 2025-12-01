import pytest
from cube_conundrum_02 import Solution

dataset = [
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
]


@pytest.fixture
def solution():
    return Solution()


def test_solution(sol: Solution):
    assert sol.find_possible_games(sol.prepare_data([dataset[0]])) == 48
    assert sol.find_possible_games(sol.prepare_data([dataset[1]])) == 12
    assert sol.find_possible_games(sol.prepare_data([dataset[2]])) == 1560
    assert sol.find_possible_games(sol.prepare_data([dataset[3]])) == 630
    assert sol.find_possible_games(sol.prepare_data([dataset[4]])) == 36
    assert sol.find_possible_games(sol.prepare_data(dataset)) == 2286
