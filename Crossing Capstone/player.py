from turtle import Turtle
import random

COLORS_SECTION = ['red', 'blue', 'green']
SPAWN = [0, -280]
class Player(Turtle):

    #Creates player avatar
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color(random.choice(COLORS_SECTION))
        self.penup()
        self.setheading(90)
        self.goto(SPAWN)

    #Functions responsible for player movement 
    def up(self):
        self.setheading(90)
        self.forward(10)
    def right(self):
        self.setheading(0)
        self.forward(10)
    def left(self):
        self.setheading(180)
        self.forward(10)

    #Function will move the player back to the starting point
    def respawn(self):
        self.goto(SPAWN)