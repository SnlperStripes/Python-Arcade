from turtle import Turtle

spawned_players = 0

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.spawn_players()

    def spawn_players(self):
        global spawned_players
        #self.speed("fastest")
        if spawned_players < 1:
            self.goto(350, 0)
            spawned_players += 1
        elif spawned_players == 1:
            self.goto(-350, 0)
            spawned_players += 1
        else:
            pass

    def move_up(self):
        cur_pos = int(self.ycor())
        move_pos_y = cur_pos + 66
        if move_pos_y < 265:
            self.sety(move_pos_y)

    def move_down(self):
        cur_pos = int(self.ycor())
        move_pos_y = cur_pos - 66
        if move_pos_y > -265:
            self.sety(move_pos_y)