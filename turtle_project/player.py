from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.setheading(90)
        self.penup()
        self.start_game()

    def move(self):
        self.fd(MOVE_DISTANCE)

    def start_game(self):
        self.goto(STARTING_POSITION)

    def at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
