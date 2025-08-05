import random
import turtle


def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


turtle.colormode(255)
turtle_object = turtle.Turtle()
directions = [0, 90, 180, 270]
turtle_object.pensize(15)
turtle_object.speed("fastest")

for _ in range(200):
    turtle_object.color(random_color())
    turtle_object.forward(30)
    turtle_object.setheading(random.choice(directions))

turtle.done()
