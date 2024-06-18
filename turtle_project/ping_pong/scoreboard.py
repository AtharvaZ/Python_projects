from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('white')
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.goto(-50, 270)
        self.write(self.l_score, align='center', font=('Arial', 25, 'normal'))
        self.goto(50, 270)
        self.write(self.r_score, align='center', font=('Arial', 25, 'normal'))

    def update_l_score(self):
        self.l_score += 1
        self.update_scoreboard()

    def update_r_score(self):
        self.r_score += 1
        self.update_scoreboard()

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        if self.l_score > self.r_score:
            self.write("GAME OVER\nLeft side WINS!!!", align="center", font=("Arial", 20, "normal"))
        else:
            self.write("GAME OVER\nRight side WINS!!!", align="center", font=("Arial", 20, "normal"))
