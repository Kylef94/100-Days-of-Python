import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

car_delay = 0
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.onkey(player.move, 'Up')
screen.listen()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car_delay += 1

    #generates cars every 6th iteration
    if car_delay == 6:
        car_manager.new_car()
        car_delay = 0

    car_manager.move_cars()

    #player collision detection
    for car in car_manager.carlist:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

    #finishing line detection
    if player.ycor() > 280:
        player.reset()
        car_manager.increase_speed()
        scoreboard.levelup()


    screen.update()
screen.exitonclick()