from turtle import Screen, Turtle

turtle_object = Turtle()
screen = Screen()


def move_forward():
    turtle_object.forward(10)


def move_backward():
    turtle_object.backward(10)


def turn_left():
    turtle_object.left(10)


def turn_right():
    turtle_object.right(10)


def clear():
    turtle_object.clear()
    turtle_object.penup()
    turtle_object.home()
    turtle_object.pendown()


screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")
screen.exitonclick()
