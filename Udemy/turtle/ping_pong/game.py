"""
Main game logic for the Ping Pong game
"""

import time
from turtle import Screen

from ball import Ball
from paddle import Paddle
from score_board import ScoreBoard

screen = Screen()
screen.bgcolor("black")
screen.title("Ping Pong Game")
screen.setup(width=800, height=600)

screen.tracer(0)

scoreboard = ScoreBoard()
right_paddle = Paddle(initial_position=(350, 0))
left_paddle = Paddle(initial_position=(-360, 0))
ball = Ball(initial_position=(0, 0), initial_direction=45)

# Set keyboard controls
screen.listen()
screen.onkey(right_paddle.move_paddle_up, "Up")
screen.onkey(right_paddle.move_paddle_down, "Down")
screen.onkey(left_paddle.move_paddle_up, "w")
screen.onkey(left_paddle.move_paddle_down, "s")

game_active = True
while game_active:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move_ball()

    # Detect collision with top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y_dir()

    # Detect collision with paddles
    if (
        ball.xcor() > 320
        and ball.distance(right_paddle) < 50
        or ball.xcor() < -330
        and ball.distance(left_paddle) < 50
    ):
        ball.bounce_x_dir()

    # Detect when right paddle misses
    if ball.xcor() > 380:
        scoreboard.left_scores()
        ball.reset_position()

    # Detect when left paddle misses
    if ball.xcor() < -390:
        scoreboard.right_scores()
        ball.reset_position()

screen.exitonclick()
