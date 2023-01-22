from turtle import Turtle

LOCATION = (-270, 280)
class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.create_board()

    #Function used to update the scoreboard when the player scores
    def scored(self):
        self.level += 1
        self.clear()
        self.create_board()
        
    #Writes the game scoreboard 
    def create_board(self):
        self.penup()
        self.goto(LOCATION)
        self.hideturtle()
        self.write(f'Level: {self.level}', align= 'center', font= ("Ariel", 14, 'normal'))

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.write(f'GAME OVER', align= 'center', font= ("Ariel", 14, 'normal'))