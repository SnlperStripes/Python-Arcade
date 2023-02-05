from turtle import Turtle

class Written(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.clear()
        self.shape("circle")
        self.speed("fastest")
        self.shapesize(0.1, 0.1)
        #self.hideturtle()
        

    def destination(self, x, y):
        self.goto(x, y)
    
    def text(self, txt):
        self.write(txt)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.hideturtle()
        self.penup()
        self.goto(0, 200)
        self.shapesize(1, 1)

    def show_score(self, txt):
        self.write(txt)