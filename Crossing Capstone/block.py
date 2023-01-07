from turtle import Turtle
from random import choice, randint

COLORS = ['blue', 'green', 'yellow', 'red', 'purple', 'orange']
class Blocks(Turtle):
    def __init__(self):
        super().__init__()
        self.spawn()


    def move(self):
        self.setheading(180)
        self.forward(10)

    def spawn(self):
        self.color(choice(COLORS))
        self.penup()
        self. shape('square')
        self.goto(320, randint(-250, 250))