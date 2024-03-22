"""Test functionality of function!"""

from lessons.sum2 import sum

def test_sum_empty() -> None:
    """Test the sum function!"""
    assert sum([]) == 0


def test_sum_one_element()-> None:
    """Test to sum of an element or list that should return a specific number!"""
    test: list[int] = [7]
    assert sum(test) == 7


def test_sum_positive() -> None:
    """Test to see if function adds all postive numbers!"""
    test: list[int] = [2, 4, 6]
    assert sum(test) == 12


def test_sum_negative() -> None:
    """Sum function should sum both positive an negative numbers!"""
    test: list[int] = [2, -2, 4]
    assert sum(test) == 4