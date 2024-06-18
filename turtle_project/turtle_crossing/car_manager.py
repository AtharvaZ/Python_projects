import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def add_new_car(self):
        chance = random.randint(1,6)
        if chance == 1:
            new = Turtle('square')
            new.penup()
            new.color(random.choice(COLORS))
            new.shapesize(stretch_wid=1, stretch_len=2)
            new.goto(290, random.randint(-270, 270))
            new.seth(180)
            self.all_cars.append(new)

    def move_car(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def speed_increase(self):
        self.car_speed += MOVE_INCREMENT

