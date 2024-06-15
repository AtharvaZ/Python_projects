from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color('white')
        self.goto(0, 280)
        self.hideturtle()
        self.write(f"Score: {self.score}", align="center", font=("Courier", 15, "normal"))

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 20, "normal"))

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Courier", 15, "normal"))
