import turtle
from turtle import Screen
import pandas


screen = Screen()

screen.title("US States Game")
IMAGE = "blank_states_img.gif"
screen.addshape(IMAGE)
turtle.shape(IMAGE)

with open("50_states.csv") as dataFile:
    data = pandas.read_csv(dataFile)


states = data.to_dict()
print(states)

answer_state = screen.textinput(title="Guess the State", prompt="What's another State?")
print(answer_state)

