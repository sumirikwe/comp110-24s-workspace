"""TODO: Describe your scene program."""
 
__author__ = "730477259"
 
from turtle import Turtle, colormode, done 
 
 
def main() -> None:
    """Create the soccer field with a ball moving towards the goal."""
    colormode(255)  # Set color mode to RGB

    field_turtle = Turtle()
    field_turtle.speed(0)
    draw_field(field_turtle, -200, -150, 400, 300)

    goal_turtle = Turtle()
    goal_turtle.speed(0)
    draw_goal(goal_turtle, -180, -20, 40, 120)

    ball_turtle = Turtle()
    ball_turtle.speed(1)
    draw_ball(ball_turtle, 180, 0, 10)

    move_ball(ball_turtle, 180, 0, -180, 0, 10, 5)

    done()
 
def draw_field(field_turtle: Turtle, x: float, y: float, width: float, height: float) -> None:
    """Draw a soccer field."""
    field_turtle.penup()
    field_turtle.goto(x, y)
    field_turtle.setheading(0)
    field_turtle.pendown()
    field_turtle.color("green")
    field_turtle.begin_fill()
    for _ in range(2):
        field_turtle.forward(width)
        field_turtle.left(90)
        field_turtle.forward(height)
        field_turtle.left(90)
    field_turtle.end_fill()

def draw_goal(goal_turtle: Turtle, x: float, y: float, width: float, height: float) -> None:
    """Draw a soccer goal."""
    goal_turtle.penup()
    goal_turtle.goto(x, y)
    goal_turtle.setheading(0)
    goal_turtle.pendown()
    goal_turtle.color("white")
    goal_turtle.fillcolor("white")
    goal_turtle.begin_fill()
    for _ in range(2):
        goal_turtle.forward(width)
        goal_turtle.left(90)
        goal_turtle.forward(height)
        goal_turtle.left(90)
    goal_turtle.end_fill()

def draw_ball(ball_turtle: Turtle, x: float, y: float, radius: float) -> None:
    """Draw a soccer ball (circle)."""
    ball_turtle.penup()
    ball_turtle.goto(x, y)
    ball_turtle.setheading(0)
    ball_turtle.pendown()
    ball_turtle.color("black")
    ball_turtle.fillcolor("white")
    ball_turtle.begin_fill()
    ball_turtle.circle(radius)
    ball_turtle.end_fill()


def move_ball(ball_turtle: Turtle, start_x: float, start_y: float, goal_x: float, goal_y: float, radius: float, distance: float) -> None:
    """Move the ball towards the goal."""
    ball_turtle.penup()
    ball_turtle.goto(start_x, start_y)
    ball_turtle.setheading(ball_turtle.towards(goal_x, goal_y))
    ball_turtle.pendown()

    while ball_turtle.distance(goal_x, goal_y) > radius:
        ball_turtle.forward(distance)


if __name__ == "__main__":
    main()
