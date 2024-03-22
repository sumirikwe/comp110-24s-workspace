"""Functions that mutate list or don't"""

__author__ = "730477259"


def remove_first(words: list[str]) -> None:
    """Remove the first string in list!"""
    words.pop(0)
    return words


def get_first(words: list[str]) -> str:
    """Obtain first string in list!"""
    a = words[0]
    return a


def get_and_remove_first(words: list[str]) -> str:
    """Get and remove first string in list"""
    a = words[0]
    words.pop(0)
    return a


animals = ["louie","bear", "bo"]
print(remove_first(animals))
print(get_first(animals))
print(get_and_remove_first(animals))