"""
Program to create a turtle race with Turtle graphics
User can bet on which turtle will win the race among the six turtles.
"""

from random import randint
from turtle import Screen, Turtle


def move_turtle(turtle: Turtle) -> None:
    turtle.forward(randint(1, 10))


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? Enter a color: "
)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# Initialize turtles at their starting position
turtles = []
for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-70 + colors.index(color) * 30)
    turtles.append(new_turtle)

# Start race
race_active = True
while race_active:
    for turtle in turtles:
        if turtle.xcor() > 220:
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print(
                    f"You won! The {winning_color} turtle is the winner! Enter to play again.",
                )
            else:
                print(
                    f"You lost! The {winning_color} turtle is the winner! Enter to play again.",
                )
            race_active = False

        move_turtle(turtle)

screen.exitonclick()
