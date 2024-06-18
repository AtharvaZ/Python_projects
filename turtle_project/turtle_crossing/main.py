import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
score  = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    #Generating new cars
    car.add_new_car()
    car.move_car()

    #Detect collision with cars
    for i in car.all_cars:
        if player.distance(i) < 20:
            game_is_on = False
            score.game_over()

    #Detect if player has reached finish line
    if player.at_finish_line():
        player.start_game()
        car.speed_increase()
        score.level()


screen.exitonclick()