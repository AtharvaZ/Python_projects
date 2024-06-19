from turtle import Turtle, Screen
import random

race_on = False

screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("Make your bet", "Enter a color of your turtle: ")
colors = ["violet", "indigo", "blue", "green", "orange", "red"]

turtles = []

for i in range(6):
    t = Turtle("turtle")
    t.color(colors[i])
    t.penup()
    t.goto(-230, -100 + 45*i)
    turtles.append(t)

if user_bet:
    race_on = True

while race_on:
    for t in turtles:

        if t.xcor() > 230:
            race_on = False
            win_color = t.pencolor()
            if win_color == user_bet:
                print(f"You won! {t.pencolor().capitalize()} won the race!")
            else:
                print(f"You lost! {t.pencolor().capitalize()} won the race!")

        random_dist = random.randint(0, 10)
        t.fd(random_dist)

screen.exitonclick()