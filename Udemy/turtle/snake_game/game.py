"""
Main game logic for the Snake game
"""

import time
from turtle import Screen

from food import Food
from scoreboard import Scoreboard
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

scoreboard = Scoreboard()
snake = Snake()
food = Food()
screen.tracer(0)  # Turns off the screen updates for performance

# Set key listeners
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

screen.update()  # Initial screen update to show the snake

game_active = True
while game_active:
    screen.update()
    time.sleep(0.1)  # Control the speed of the game
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.respawn()
        snake.extend_snake()
        scoreboard.increase_score()

    # Detect collision with walls
    if (
        snake.head.xcor() > 290
        or snake.head.xcor() < -290
        or snake.head.ycor() > 290
        or snake.head.ycor() < -290
    ):
        game_active = False
        scoreboard.game_over()

    # Detect collision with snake's body (head hits body)
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_active = False
            scoreboard.game_over()

screen.exitonclick()
