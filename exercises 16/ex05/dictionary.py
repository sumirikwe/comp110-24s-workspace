"""Dictionary Utility Functions!"""

__author__ = "730477259"

import random

def invert(word: dict[str, str]) -> dict[str, str]:
    """Invert, strings in a dictionary!"""
    new_dict: dict[str, str] = {}
    for keys in word:
        if word[keys] in new_dict:
            raise KeyError("error message of your choice here!")
        new_dict[word[keys]] = keys

    print(new_dict)
    return new_dict

invert({'a': 'z', 'b' : 'y', 'c': 'x'})
invert({'kris': 'jordan', 'michael': 'jackson'})


def favorite_colors(color: dict[str, str]) -> str:
    """Print the favorite color!"""
    counter: int = 0
    new_dict: dict[str] = {}
    final_value = ""
    for keys in color:
        value = color[keys]
        if color[keys] in new_dict:
            new_dict[value] += 1
        else:
            new_dict[value] = 1

        if new_dict[value] > counter:
            counter = new_dict[value]
            final_value = value
    
    return final_value

print(favorite_colors({"Marc": "yellow", "Ezri": "blue", "Kris": "blue", "sam": "yellow", "Tree": "yellow"}))


def count(num: list[str]) -> dict[str, int]:
    """Count what string appears the most!"""
    new_dict: dict[str] = {}
    for key in num:
        if key in new_dict:
            new_dict[key] += 1
        else:
            new_dict[key] = 1
    return new_dict


print(count(["car", "apple", "boy", "angry", "boy", "car", "car"]))


def alphabetizer(abc: list[str]) -> dict[str, list[str]]:
    "print the first letter of a string!"
    new_dict: dict[str, list[str]] = {}
    for elem in abc:
        first_letter = elem[0].lower()
        
        if first_letter not in new_dict:
            new_dict[first_letter] = [elem]
        else:
            new_dict[first_letter] += [elem]
    
    return new_dict


print(alphabetizer(["cat", "apple", "boy", "angry", "bad", "car", "coochie"]))


def update_attendance(attend: dict[str, list[str]], day: str, stu: str) -> dict[str, list[str]]:
    """Update dictionaries!"""
    new_dict: dict[str, list[str]] = {}
    if day in attend:
        new_list: list[str] = []
        for elem in attend[day]:
            new_list.append(elem)
        
        if stu not in new_list:
            new_list.append(stu)
            new_dict[day] = new_list
        else:
            new_dict[day] = [stu]
        
        for other_day in attend:
            if other_day != day:
                new_dict[other_day] = attend[other_day]
    
    return new_dict


attendance_log: dict = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
update_attendance(attendance_log, "Tuesday" , "Vrinda")
update_attendance(attendance_log, "Wednesday" , "Kaleb")
print(attendance_log)