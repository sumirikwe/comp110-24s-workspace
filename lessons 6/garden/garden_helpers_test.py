"""Test my garden functions."""

__author__ = "730477259"

from lessons.garden.garden_helpers import add_by_kind, add_by_date, lookup_by_kind_and_date

def test_add_by_kind() -> None:
    """Test the add by kind function!"""
    test: dict[str, list[str]] = {"flower": ["roses", "tulips"], "vegetable": ["tomato"]}
    new: str = "cars"
    strings: str = "chevy"
    add_by_kind(test, new, strings)
    assert test == {"flower": ["roses", "tulips"], 'vegetable': ["tomato"], "cars": ["chevy"]}


def test_edge_add_by_kind() -> None:
    """Test if the add by kind function mutates dict when empty!"""
    test: dict[str, list[str]] = {}
    new: str = "cars"
    strings: str = "chevy"
    add_by_kind(test, new, strings)
    assert test == {"cars": ["chevy"]}


def test_add_by_date() -> None:
    """Test the add by date function!"""
    test: dict[str, list[str]] = {"soccer season": ["august", "september", "october"], "volleyball": ["june, july"]}
    new: str = "basketball season"
    strings: str = "march"
    add_by_date(test, new, strings)
    assert test == {"soccer season": ["august", "september", "october"], "volleyball": ["june, july"], "basketball season": ["march"]}


def test_edge_add_by_date() -> None:
    """test what heppens to the fucntion when the dict is empty!"""
    test: dict[str, list[str]] = {}
    new: str = "basketball season"
    strings: str = "march"
    add_by_date(test, new, strings)
    assert test == {"basketball season": ["march"]}


def test_lookup_by_kind_and_date() -> None:
    """Test how the two functions work together!"""
    test: dict[str, list[str]] = {"soccer season": ["august", "september", "october"], "basketball season": ["march"]}
    quiz: dict[str, list[str]] = {"field": ["october"], "court": ["march"]}
    assert lookup_by_kind_and_date(test, quiz, "soccer season", "field") == "soccer seasons to plant in field: ['october']"


def test_edge_lookup_by_kind_and_date() -> None:
    "Test what happens when there are no season to plain in a month"
    test: dict[str, list[str]] = {"soccer season": ["august", "september", "october"], "basketball season": ["march"]}
    quiz: dict[str, list[str]] = {"field": ["october"], "court": ["march"]}
    assert lookup_by_kind_and_date(test, quiz, "basketball season", "field") == "No basketball seasons to plant in field."