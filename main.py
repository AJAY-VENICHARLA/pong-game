from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("PONG GAME")
screen.tracer(0)
screen.listen()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = ScoreBoard()


def go_up():
    new_y = r_paddle.ycor()+20
    r_paddle.goto(r_paddle.xcor(), new_y)


def go_down():
    new_y = r_paddle.ycor()-20
    r_paddle.goto(r_paddle.xcor(), new_y)


def go_above():
    new_y = l_paddle.ycor()+20
    l_paddle.goto(l_paddle.xcor(), new_y)

def go_below():
    new_y = l_paddle.ycor()-20
    l_paddle.goto(l_paddle.xcor(), new_y)


screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_above, "w")
screen.onkey(go_below, "s")
game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # detects collision with wall
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce_y()

    # detects collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
