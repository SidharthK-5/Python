"""
Class for managing the snake
"""

from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments: list[Turtle] = []
        self.create_snake()
        self.head: Turtle = self.segments[0]

    def create_snake(self):
        """
        Create the initial snake segments and move them into position.
        """
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position: tuple[int, int]):
        """
        Add a new segment to the snake.
        """
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend_snake(self):
        """
        Extend the snake by adding a new segment at the end.
        """
        self.add_segment(self.segments[-1].position())

    def move(self):
        """
        Move the snake segments forward.
        """
        for segment_id in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment_id - 1].xcor()
            new_y = self.segments[segment_id - 1].ycor()
            self.segments[segment_id].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)  # Move the head of the snake forward

    def up(self):
        """
        Move the snake up.
        """
        if self.head.heading() != DOWN:  # Prevent the snake from going back on itself
            self.head.setheading(UP)

    def down(self):
        """
        Move the snake down.
        """
        if self.head.heading() != UP:  # Prevent the snake from going back on itself
            self.head.setheading(DOWN)

    def left(self):
        """
        Move the snake left.
        """
        if self.head.heading() != RIGHT:  # Prevent the snake from going back on itself
            self.head.setheading(LEFT)

    def right(self):
        """
        Move the snake right.
        """
        if self.head.heading() != LEFT:  # Prevent the snake from going back on itself
            self.head.setheading(RIGHT)
