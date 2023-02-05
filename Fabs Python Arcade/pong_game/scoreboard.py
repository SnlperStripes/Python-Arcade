from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.score_left_p = 0
        self.score_right_p = 0
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"{self.score_left_p} | {self.score_right_p}", align=ALIGNMENT, font=FONT)
