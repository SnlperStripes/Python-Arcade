from turtle import Turtle, Screen
from pong_game.player import Player
from pong_game.ball import Ball, spawn_right, ball_forward_speed
from time import sleep
from pong_game.scoreboard import Scoreboard


def pong_main():

    monitor = Screen()
    monitor.setup(800, 600)
    monitor.bgcolor("black")
    monitor.tracer(0)

    p2 = Player()
    p1 = Player()

    monitor.listen()

    monitor.onkey(p1.move_up, "w")
    monitor.onkey(p1.move_down, "s")

    monitor.onkey(p2.move_up, "Up")
    monitor.onkey(p2.move_down, "Down")

    def spawn_ball():
        ball = Ball()

    ball = Ball(dir="right")

    scoreboard = Scoreboard()

    game_is_on = True

    while game_is_on:
        sleep(0.01)
        if ball.distance(p2) < 77 and ball.xcor() > 350:
            new_dir = ball.heading() + 90
            ball.setheading(new_dir)
            #ball_forward_speed += 1
        elif ball.distance(p1) < 77 and ball.xcor() < -350:
            new_dir = ball.heading() + 90
            ball.setheading(new_dir)
            #ball_forward_speed += 1
        
        if ball.ycor() > 286:
            new_heading = ball.heading() + 45
            ball.setheading(new_heading)
        elif (ball.xcor() > 413):
            print("GOAL SCORED RIGHT")
            scoreboard.score_left_p += 1
            scoreboard.clear()
            scoreboard.update_scoreboard()
            del ball
            ball = Ball(dir="left")
                
        elif ball.ycor() < -286:
            new_heading = ball.heading() + 45
            ball.setheading(new_heading)
        elif (ball.xcor() < -413):
            print("GOAL SCORED LEFT")
            scoreboard.score_right_p += 1
            scoreboard.clear()
            scoreboard.update_scoreboard()
            del ball
            ball = Ball(dir="right")

        monitor.update()
        ball.move_forward()






