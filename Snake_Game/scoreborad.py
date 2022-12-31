from turtle import Turtle

START_POINT = (0,280)
FONT_STYLE = ('Arial', 12, 'normal')

class ScoreBoard(Turtle):

   def __init__(self):
      super().__init__()
      self.penup()
      self.hideturtle()
      self.goto(START_POINT)
      self.score = 0
      self.color("white")
      self.update_scoreboard()
      
   
   def game_over(self):
      self.goto(0, 0)
      self.write("Game Over",align='center',font= FONT_STYLE)
   

   def update_scoreboard(self):
      self.write(f"Score: {self.score}", move= False, align= 'center',font= FONT_STYLE)
      
   def scored(self):
      self.score += 1
      self.clear()
      self.update_scoreboard()
   

