"""Summing the elements of a list using different loops."""

__author__ = "730477259"


def w_sum(vals: list[float]) -> float:
    """Add values using while!"""
    idx: int = 0
    total: float = 0.0

    while idx < len(vals):
        total += vals[idx]
        idx += 1
    return total


def f_sum(vals: list[float]) -> float:
    """Add values using for... in!"""
    totals: float = 0.0
    for elem in vals:
        totals += elem
    return totals


def f_range_sum(vals: list[float]) -> float:
    """Add values using range!"""
    summ: float = 0.0
    for index in range(0, len(vals)):
        summ += vals[index]
    return summ