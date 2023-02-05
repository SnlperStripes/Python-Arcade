from turtle import Turtle
from random import randint
#from scoreboard import Scoreboard

spawn_right = True
ball_forward_speed = 0.1

class Ball(Turtle):
    def __init__(self, dir):
        super().__init__()
        #self.spawn_ball()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.speed(10)
        self.spawn_direction(direction=dir)
        """ if spawn_right:
            self.setheading(45)
        else:
            self.setheading(225) """


    def move_forward(self):
        #self.detect_collision()
        self.forward(6)


    def spawn_direction(self, direction):
        if direction == "right":
            self.setheading(45)
        elif direction == "left":
            self.setheading(225)



    #def detect_collision(self):
        """ if self.ycor() > 286:
            new_heading = self.heading() + 45
            self.setheading(new_heading)
        elif (self.xcor() > 413):
            print("GOAL SCORED RIGHT")
            scoreboard.score_right_p += 1
            scoreboard.clear()
            scoreboard.update_scoreboard()
            
        elif self.ycor() < -286:
            new_heading = self.heading() + 45
            self.setheading(new_heading)
        elif (self.xcor() < -413):
            print("GOAL SCORED LEFT")
            scoreboard.score_right_p += 1
            scoreboard.clear()
            scoreboard.update_scoreboard() """