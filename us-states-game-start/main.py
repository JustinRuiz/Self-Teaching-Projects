import turtle
import pandas

screen = turtle.Screen()
screen.title('States of the United States')

image = 'blank_states_img.gif'
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv('50_states.csv')
all_states = data.state.to_list()
guess_state = []

while len(guess_state) < 50:

    answer_state = screen.textinput(title=f'{len(guess_state)}/50 Correct', prompt= "Name the State").title()

    if answer_state in all_states:
        guess_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data =data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())

screen.exitonclick()