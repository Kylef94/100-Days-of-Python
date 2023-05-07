from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:


    def __init__(self):
        self.carlist = []
        self.carspeed = STARTING_MOVE_DISTANCE



    def new_car(self):
        car = Turtle()
        car.penup()
        car.shape('square')
        car.seth(180)
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.color(random.choice(COLORS))
        starting_y = random.randrange(-250,250, 5)
        car.goto(300, starting_y)
        self.carlist.append(car)

    def move_cars(self):
        for car in self.carlist:
            car.fd(self.carspeed)

    def increase_speed(self):
        self.carspeed = STARTING_MOVE_DISTANCE + MOVE_INCREMENT