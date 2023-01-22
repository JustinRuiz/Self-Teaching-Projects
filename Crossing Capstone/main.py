from turtle import Screen, Turtle
import time
from player import Player
from block import Blocks
from scoreboard import Level

screen = Screen()
screen.setup(width= 600, height= 600)
screen.title("Crossing")
screen.tracer(0)
screen.listen()

#Objects used throughotut the game 
player = Player()
car = Blocks()
score = Level()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    #Keeps the cars in motion spawning
    car.spawn()
    car.move()

    #Detect collision with car
    for i in car.cars:
        if i.distance(player) < 20:
            game_is_on = False
            score.game_over()

    #What would occur when the player reaches the goal
    if player.ycor() == 280:
        score.scored()
        car.pace *= 1.5
        player.respawn()
    
    #Player controls
    screen.onkeypress(player.up, 'Up')
    screen.onkeypress(player.left, 'Left')
    screen.onkeypress(player.right, 'Right')

screen.exitonclick()