from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.title("Pong")
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.tracer(0)
screen.listen()

l_paddle = Paddle((-350,0))
r_paddle = Paddle((350,0))
puck = Ball()
score = Scoreboard()

game_on = True

screen.onkeypress(l_paddle.paddle_up, 'w')
screen.onkeypress(l_paddle.paddle_down, 's')

screen.onkeypress(r_paddle.paddle_up, 'Up')
screen.onkeypress(r_paddle.paddle_down, 'Down')

while game_on:
    screen.update()
    time.sleep(0.1)
    puck.movement()

    if puck.ycor() > 280 or puck.ycor() < -280:
        puck.y_bounce()

    if puck.distance(r_paddle) < 50 and puck.xcor() > 320 or puck.distance(l_paddle) < 50 and puck.xcor() < -320:
        puck.x_bounce()
        puck.ball_speed_up()

    if puck.xcor() > 380:
        puck.reset()
        score.l_point()

    if puck.xcor() < -380:
        puck.reset()
        score.r_point()

screen.exitonclick()