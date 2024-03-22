"""List utility functions."""

__author__ = "730477259"


def all(num1: list[int], num2: int) -> bool:
    """Find the same integers!"""
    if len(num1) == 0:
        return False
    
    idx: int = 0
    while idx < len(num1):
        if num1[idx] == num2:
            idx += 1
        else:
            print("False")
            return False
    print("True")
    return True


def max(input: list[int]) -> int:
    """Find max value!"""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    
    idx: int = 0
    max_num: int = input[0]
    while idx < len(input):
        if input[idx] > max_num:
            max_num = input[idx]
        idx += 1
    print(max_num)
    return max_num


def is_equal(val_1: list[int], val_2: list[int]) -> bool:
    """Find equal list!"""
    if len(val_1) != len(val_2):
        print("False")
        return False
    if len(val_1) == 0 and len(val_2) == 0:
        print("True")
        return True
    if len(val_1) == len(val_2):
        for elem in val_1 and val_2:
            if val_1 == val_2:
                print("True")
                return True
            else:
                print("False")
                return False
    return True     

def extend(a: list[int], b: list[int]) -> None:
    """Appedn lists!"""
    for numbers in b:
        a.append(numbers)
    print(a)
    return None
