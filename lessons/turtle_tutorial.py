"""Turtle Tutorial!!!"""

from turtle import Turtle, colormode, done
colormode(255)
leo: Turtle = Turtle()


bob: Turtle = Turtle()

side_length: int = 300
 
i: int = 0
while (i < 3):
    bob.forward(side_length)
    bob.left(120)
    i = i + 1
    side_length = side_length * 0.97
