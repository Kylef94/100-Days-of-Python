import random
from turtle import Turtle, Screen

screen = Screen()
timmy = Turtle()
timmy.shape("turtle")
timmy.color("coral")
timmy.pen(pensize=2, speed=30)
screen.colormode(255)
# for i in range(3,10):
#     for j in range(i)hjvv :
#         timmy.fd(100)
#         timmy.right(360/i)

# while timmy:
#    timmy.seth(90 * (random.randint(0,3)))
#    timmy.fd(20)

def random_color():
   r = random.randint(0,255)
   g = random.randint(0, 255)
   b = random.randint(0, 255)
   t = (r,g,b)
   return t

for i in range(0,360, 5):
   timmy.color(random_color())
   timmy.seth(i)
   timmy.circle(100)

screen.exitonclick()