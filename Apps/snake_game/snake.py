from turtle import Turtle

STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.new_snake()
        self.head = self.segments[0]


    def new_snake(self):
        for position in STARTING_POS:
           self.add_segment(position)

    def add_segment(self, position):
        new_turtle = Turtle("square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.setpos(position)
        self.segments.append(new_turtle)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.new_snake()
        self.head = self.segments[0]
    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.head.forward(MOVE_DIST)

    def u(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def d(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def l(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def r(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)