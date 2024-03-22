"""Dictionary unit tests!!!"""

__author__ = "730477259"


from exercises.ex05.dictionary import invert, favorite_color, count, alphabetizer, update_attendance
import pytest


def test_invert() -> None:
    """Test the invert function usecase1."""
    test: dict[str, str] = {"apple": "cat", "orange": "dog", "grape": "fish"}
    assert invert(test) == {'cat': 'apple', 'dog': 'orange', 'fish': 'grape'}


def test_use_invert() -> None:
    """Test the invert function usecase2."""
    test: dict[str, str] = {"harden": "james", "lebron": "james"}
    assert pytest.raises(KeyError, invert, test)


def test_edge_invert() -> None:
    """Test the invert function edge case."""
    test: dict[str, str] = {}
    assert invert(test) == {}


def test_favorite_color() -> None:
    """Test the favorite color function usecase1."""
    test: dict[str, str] = {"Marc": "yellow", "Ezri": "purple", "Kris": "blue", "sam": "purple"}
    assert favorite_color(test) == "purple"


def test_use_favorite_color() -> None:
    """Test the favorite color function usecase2 - color that shows up first should be printed!"""
    test: dict[str, str] = {"Marc": "yellow", "Ezri": "yellow", "Kris": "purple", "sam": "purple"}
    assert favorite_color(test) == "yellow"


def test_edge_favorite_color() -> None:
    """Test the favorite color function edge."""
    test: dict[str, str] = {}
    assert favorite_color(test) == ""


def test_count() -> None:
    """Test the count function usecase1."""
    test: list[str] = ["sam", "ben", "sam", "alex", "sam"]
    assert count(test) == {'sam': 3, 'ben': 1, 'alex': 1}


def test_use_count() -> None:
    """Test the count function usecase2 - test to see what happens if there are two names with the count."""
    test: list[str] = ["sam", "alex", "sam", "alex"]
    assert count(test) == {'sam': 2, 'alex': 2}


def test_egde_count() -> None:
    """Test the count function edgecase."""
    test: list[str] = []
    assert count(test) == {}


def test_alphabetizer() -> None:
    """Test the alphabetizer function usecase1 - see if it works."""
    test: list[str] = ["unc", "duke", "uncg", "state"]
    assert alphabetizer(test) == {'u': ['unc', 'uncg'], 'd': ['duke'], 's': ['state']}


def test_use_alphabetizer() -> None:
    """Test the alphabetizer function usecase2 - see if the function groups capitol letters with lowercase."""
    test: list[str] = ["UNC", "duke", "uncg", "state"]
    assert alphabetizer(test) == {'u': ['UNC', 'uncg'], 'd': ['duke'], 's': ['state']}


def test_edge_alphabetizer() -> None:
    """Test the alphabetizer function edgecase - see what happens if an empty list is input."""
    test: list[str] = []
    assert alphabetizer(test) == {}


def test_update_attendance() -> None:
    """Test the update function usecase1 - add a student to an existing day."""
    test: dict[str, list[str]] = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    day: str = "Tuesday"
    student: str = "Samuel"
    update_attendance(test, day, student) 
    assert test[day] == ["Alyssa", "Samuel"]


def test_use_update_attendance() -> None:
    """Test the update function usecase2 - add a student to a new day."""
    test: dict[str, list[str]] = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa", "Samuel"]}
    day: str = "Friday"
    student: str = "Drake"
    update_attendance(test, day, student)
    assert test[day] == ["Drake"]


def test_edge_update_attendance() -> None:
    """Test the update function edgecase - add an existing student to an existing date."""
    test: dict[str, list[str]] = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa", "Samuel"]}
    day: str = "Monday"
    student: str = "Samuel"
    update_attendance(test, day, student) 
    assert test[day] == ["Vrinda", "Kaleb", "Samuel"]
