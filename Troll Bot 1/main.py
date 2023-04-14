import turtle
import troll_response

screen = turtle.Screen()

image = "robot-talk.gif"

screen.addshape(image)
turtle.shape(image)

still_asking = True

r = turtle.Turtle()
r.hideturtle()
r.penup()
r.goto(0, -234.0)

while still_asking:

    user_input = screen.textinput(title= "User Entry", prompt= "What do you ant to know. Math, Reading, Geography")
    
    r.clear()

    if user_input.title() == 'Math':
        
        math_reply = screen.textinput(title= "Math Question", prompt= "What do you want to know about?")

        r.write(troll_response.math_logic[math_reply.title()])

    elif user_input.title() == "Reading":

        reading_reply = screen.textinput(title= "Reading Question", prompt= "What do you want to know about?")

        r.write(troll_response.reading_logic[reading_reply.title()])

    elif user_input.title() == "Geography":

        geo_reply = screen.textinput(title= "Geography Question", prompt= "What do you want to know about?")

        r.write(troll_response.geography_logic[geo_reply.title()])

    else:

        r.write("That's a invalid response")
        

    if user_input.title() == 'Exit':

        still_asking = False


turtle.exitonclick()
