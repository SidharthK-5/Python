"""
Class to manage food
"""

import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("blue")
        self.penup()
        self.speed("fastest")

        # Set initial position
        x_init = random.randint(-280, 280)
        y_init = random.randint(-280, 280)
        self.goto(x_init, y_init)

    def respawn(self):
        """
        Respawn the food at a new random location.
        """
        x_new = random.randint(-280, 280)
        y_new = random.randint(-280, 280)
        self.goto(x_new, y_new)
