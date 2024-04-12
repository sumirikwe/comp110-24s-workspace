"""Writing a Recursive Function!"""

__author__ = "730477259"


def f(n: int, k: int) -> int:
    """Multiply N and K!!!"""
    if n == 0:
        return 0
    else:
        return k + f(n - 1, k)