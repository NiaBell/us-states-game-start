import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
IMAGE = "blank_states_img.gif"
screen.addshape(IMAGE)
turtle.shape(IMAGE)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

writing = turtle.Turtle()

guessed_states=[]
score = 0

states = data["state"]
states = states.tolist()

while len(guessed_states) < 50:
    answer_state = (screen.textinput(title= f"{len(guessed_states)} Correct States", prompt="What's another State?")).title()

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")

        break
    if answer_state in states:
        writing.penup()
        state_data = data[data.state == answer_state]
        writing.goto(int(state_data.x),int(state_data.y))
        writing.write(answer_state)
        guessed_states.append(answer_state)
        score += 1

#states to learn.csv