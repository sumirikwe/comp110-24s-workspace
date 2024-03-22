"""Test my mutating function"""

from lessons.mutations.mutating_functions import remove_first, get_first, get_and_remove_first

def test_remove_first() -> None:
    """Test if the function removes the first string."""
    test = ["unc", "duke", "wake", "state"]
    remove_first(test)
    assert test == ["duke", "wake", "state"]


def test_get_first() -> None:
    """Test if the function produces the first string."""
    test = ["unc", "duke", "wake"]
    real_test: str = get_first(test)
    assert real_test == "unc"
    assert test == ["unc", "duke", "wake"]


def test_get_and_remove_first() -> None:
    """Test if the functionlity of the get and remove function."""
    test = ["unc", "duke", "wake"]
    assert get_and_remove_first(test) == "unc"
    assert test == ["duke", "wake"]