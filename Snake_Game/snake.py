from turtle import Turtle

STARTING_POSITION = [(0,0), (-20,0), (-40,0)]
MOVEMENT = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake(Turtle):

    def __init__(self):
        super().__init__()
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.tail = self.segments[-1]
        
    def create_snake(self):
        """Creates the starting 3 snake segments"""
        for i in STARTING_POSITION:
            self.add_segment(i)

    def add_segment(self, position):
        new_square = Turtle(shape='square')
        new_square.penup()
        new_square.color('white')
        new_square.goto(position)
        self.segments.append(new_square)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        """Moves every segment of the snake"""
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVEMENT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)