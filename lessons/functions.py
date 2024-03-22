"""Demonstrates functions"""
from random import randint

y: str = print("Hello!")
print(y)

x: int = round(10.25)
print(x)

z: int = randint(1, 7)
print(z)

"""Example functions to learn definition and calling syntax"""

def my_max(number1: int, number2: int) -> int:
    """returns the maximum value out two numbers"""
    if number1 >= number2:
        return number1
    else:
        return number2
    
max_number: int = my_max(1,10)
other_max_number: int = my_max(11,3)
print(other_max_number)

    
