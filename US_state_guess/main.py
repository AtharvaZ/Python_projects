import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S state games")
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

data = pandas.read_csv("50_states.csv")
state_names = data.state.to_list()

guess = []
left_state = []

while len(guess)<50:

    name = screen.textinput(title=f"{len(guess)}/50 states correct",
                            prompt="Which other US state name?").title()
    if name == "Exit":
        left_state = [state for state in state_names if state not in guess]
        new_data = pandas.DataFrame(left_state)
        new_data.to_csv("missing_state.csv")
        break
    if name in state_names:
        guess.append(name)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == name]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(name)

screen.exitonclick()
