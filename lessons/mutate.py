"""Mutating functions."""

__author__ = "730477259"


def manual_append(numbers: list[int], num1: int) -> None:
    """Adding a random number to a the end of a list."""
    numbers.append(num1)


abc_123: list[int] = [1, 2, 3]
manual_append(abc_123, 99)

print(abc_123)


def double(numbers: list[int]) -> None:
    """Double or nothing!"""
    count = 0
    while count < len(numbers):
        numbers[count] *= 2
        count += 1


double(abc_123)

print(abc_123)