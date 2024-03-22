"""Sum all elements in a list!"""


def sum(elem: list[int]) -> int:
    """Sum all elements in a list!"""
    total: int = 0
    for elements in elem:
        total += elements
    return total