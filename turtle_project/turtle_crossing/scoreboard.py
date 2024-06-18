from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level_num = 0
        self.hideturtle()
        self.teleport(-235, 270, fill_gap=False)
        self.write(f"Level: {self.level_num}", align="center", font=FONT)

    def level(self):
        self.level_num += 1
        self.clear()
        self.write(f"Level: {self.level_num}", align="center", font=FONT)

    def game_over(self):
        self.teleport(0, 0, fill_gap=False)
        self.write(f"GAME OVER", align="center", font=FONT)


