""" Tests for Secret Entrance - Part 2 """
from secret_entrance_02 import get_password, prepare_data

DATA = [
    "L68",
    "L30",
    "R48",
    "L5",
    "R60",
    "L55",
    "L1",
    "L99",
    "R14",
    "L82",
]

def test_get_password():
    """ Test the password calculation with the sample data """
    formatted = prepare_data(DATA)
    assert get_password(formatted) == 6
