import scoreboard
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong")
screen.tracer(0)
race_to = screen.textinput("Race to", "Enter total match points:")

t2 = Turtle()
t2.hideturtle()
t2.color('white')
t2.teleport(0, 300, fill_gap=False)
t2.rt(90)

for i in range(15):
    t2.pendown()
    t2.fd(20)
    t2.penup()
    t2.fd(20)

r_paddle = Paddle((370, 0))
l_paddle = Paddle((-370, 0))
ball = Ball()
score = Scoreboard()

#moving the paddle

screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_wall()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 350:
        ball.bounce_pad()
        score.update_r_score()

    if ball.distance(l_paddle) < 50 and ball.xcor() < -350:
        ball.bounce_pad()
        score.update_l_score()

    if ball.xcor() > 370:
        ball.refresh()
        score.update_l_score()

    if ball.xcor() < -370:
        ball.refresh()
        score.update_r_score()

    if score.l_score == int(race_to) or score.r_score == (race_to):
        game_is_on = False
        t2.clear()
        score.game_over()

screen.exitonclick()
