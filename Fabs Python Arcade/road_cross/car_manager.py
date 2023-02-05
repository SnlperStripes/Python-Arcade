from turtle import Turtle
from random import choice
from random import randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
ACTUAL_MOVE_DISTANCE = 5
X_SPAWN = 300

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(1, 2)
        self.penup()
        self.color(choice(COLORS))
        self.seth(180)
        rand_y = randint(-230, 230)
        self.goto(X_SPAWN, rand_y)


    def move_car(self):
        self.forward(ACTUAL_MOVE_DISTANCE)

    def increase_movement_speed(self):
        global ACTUAL_MOVE_DISTANCE, MOVE_INCREMENT
        ACTUAL_MOVE_DISTANCE += MOVE_INCREMENT