"""Splitting a dictionary into two lists!"""

__author__ = "730477259"


def get_keys(a: dict[str, int]) -> list[str]:
    """Print keys of a dictionary!"""
    list_1: list[str] = []
    for keys in a:
        list_1.append(keys)
    
    return list_1


def get_values(a: dict[str, int]) -> list[int]:
    """Produce all of the values of the DICT!"""
    list_1: list[int] = []
    for keys in a:
        list_1.append(a[keys])

    return list_1