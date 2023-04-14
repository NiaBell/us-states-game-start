import turtle
from turtle import Screen
import pandas


screen = Screen()

screen.title("US States Game")
IMAGE = "blank_states_img.gif"
screen.addshape(IMAGE)
turtle.shape(IMAGE)

writing = turtle.Turtle()


with open("50_states.csv") as dataFile:
    data = pandas.read_csv(dataFile)

states = data["state"]
states = states.tolist()

# state_x = data["state"]
# states = states.tolist()
#
# state_y = data["state"]
# states = states.tolist()




answer_state = (screen.textinput(title="Guess the State", prompt="What's another State?")).title()
#
#
if answer_state in states:
    writing.penup()
    writing.goto(139,-77)
    writing.write(answer_state)


answer_state = (screen.textinput(title="Guess the State", prompt="What's another State?")).title()