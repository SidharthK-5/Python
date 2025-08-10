import random
import turtle

import colorgram


def extract_colors(image_path, num_colors):
    colors = colorgram.extract(image_path, num_colors)
    return [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]


image_path = "data/hirst_painting.jpg"
colors = extract_colors(image_path, 30)

turtle.colormode(255)
turtle_object = turtle.Turtle()
turtle_object.speed("fastest")
turtle_object.penup()
turtle_object.hideturtle()

# Move the turtle to the starting position
turtle_object.setheading(225)
turtle_object.forward(300)
turtle_object.setheading(0)
num_dots = 100

for dot_count in range(1, num_dots + 1):
    turtle_object.dot(20, random.choice(colors))
    turtle_object.forward(50)

    if dot_count % 10 == 0:
        turtle_object.setheading(90)
        turtle_object.forward(50)
        turtle_object.setheading(180)
        turtle_object.forward(500)
        turtle_object.setheading(0)

screen = turtle.Screen()
screen.exitonclick()
