import random
import turtle


def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


turtle.colormode(255)
turtle_object = turtle.Turtle()
turtle_object.speed("fastest")


def draw_spirograph(gap_size):
    for _ in range(360 // gap_size):
        turtle_object.color(random_color())
        turtle_object.circle(100)
        turtle_object.setheading(turtle_object.heading() + gap_size)


draw_spirograph(5)
screen = turtle.Screen()
screen.exitonclick()
