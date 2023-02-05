import time
from turtle import Screen
from road_cross.player import Player
from road_cross.car_manager import CarManager, ACTUAL_MOVE_DISTANCE
from road_cross.scoreboard import Scoreboard

def road_cross_main():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)

    def next_level():
        player.goto(0, -280)
        new_car.increase_movement_speed()
        print("Movement speed increased")
        scoreboard.increase_level()
        scoreboard.clear()
        scoreboard.current_level()

    player = Player()

    scoreboard = Scoreboard()
    scoreboard.current_level()      #display level

    screen.listen()
    screen.onkey(player.move_up, "Up")

    game_is_on = True
    counter = 0
    new_car = CarManager()

    cars = [new_car]


    while game_is_on:
        if player.ycor() >= 200:
            next_level()

        counter += 1
        if counter >= 6:
            new_player = CarManager()
            cars.append(new_player)
            counter = 0

        for car in cars:
            car.move_car()
            #car.forward(ACTUAL_MOVE_DISTANCE)
            if player.distance(car) < 20:
                scoreboard.game_over()
                game_is_on = False

        time.sleep(0.1)
        screen.update()

    screen.exitonclick()