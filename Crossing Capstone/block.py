from turtle import Turtle
from random import choice, randint

COLORS = ['blue', 'green', 'red', 'purple', 'orange']
class Blocks(Turtle):

    
    def __init__(self):
        self.pace = 10
        self.cars = []

    #Function responsible for moving the blocks across the screen
    def move(self):
        for cars in self.cars:
            cars.setheading(180)
            cars.forward(self.pace)

    def spawn(self):
        '''Creates a new block outside the player's view.'''
        random_choice = randint(1, 6)
        
        if random_choice == 1:
            new_car = Turtle()
            new_car.color(choice(COLORS))
            new_car.penup()
            new_car.shape('square')
            new_car.shapesize(stretch_len= 2)
            new_car.goto(320, randint(-250, 250))
            self.cars.append(new_car)