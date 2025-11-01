"""
Class to manage the ball behavior in the ping pong game.
"""

from turtle import Turtle


class Ball(Turtle):
    def __init__(
        self, initial_position: tuple[int, int] = (0, 0), initial_direction: int = 90
    ):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(initial_position)
        self.speed("slowest")
        self.setheading(initial_direction)
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1  # For adjusting ball speed in game loop

    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x_dir()
        self.ball_speed = 0.1

    def bounce_y_dir(self):
        self.y_move *= -1

    def bounce_x_dir(self):
        self.x_move *= -1
        self.ball_speed *= 0.75  # Increase speed by reducing sleep time
