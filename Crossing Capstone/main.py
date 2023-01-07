from turtle import Screen, Turtle
import time
from player import Player
from block import Blocks

screen = Screen()
screen.setup(width= 600, height= 600)
screen.title("Crossing")
screen.tracer(0)
screen.listen()

player = Player()
block = Blocks()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    block.move()

    screen.onkeypress(player.up, 'Up')
    screen.onkeypress(player.left, 'Left')
    screen.onkeypress(player.right, 'Right')

screen.exitonclick()