""" Test for Gift Shop - Part 2 """
from gift_shop_02 import get_solution, format_data, populate_ranges

DATA = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

def test_solution():
    """ test the solution with the provided example """
    assert get_solution(populate_ranges(format_data(DATA))) == 4174379265
