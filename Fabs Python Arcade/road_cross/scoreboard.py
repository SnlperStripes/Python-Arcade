from turtle import Turtle

FONT = ("Courier", 24, "normal")

Level = 1

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER")

    def current_level(self):
        self.goto(-280, 260)
        self.write(f"Level: {Level}", font= FONT)

    def increase_level(self):
        global Level
        Level += 1