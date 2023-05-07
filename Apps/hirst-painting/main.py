# import colorgram
#
# pic = colorgram.extract("image.jpeg", 25)
#
# colors = []
#
# for i in range(len(pic)):
#     color = pic[i].rgb
#     colors.append((color.r, color.g, color.b))
#
# print(colors)


from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=750, height=750, startx=650, starty=650)
t = Turtle()
t.shape("turtle")
t.color("coral")
t.speed("fastest")
screen.colormode(255)

def random_color():
    color_list = [(1, 13, 31), (52, 25, 17), (219, 127, 106), (9, 105, 160), (242, 214, 69), (150, 84, 39), (215, 87, 64), (164, 162, 32), (158, 6, 24), (157, 62, 102), (11, 63, 32), (97, 6, 19), (207, 74, 104), (10, 97, 58), (0, 63, 145), (173, 135, 162), (7, 172, 216), (158, 34, 24), (3, 213, 207), (8, 140, 85), (145, 227, 216)]
    max = len(color_list) - 1
    c = color_list[random.randint(0, max)]
    return c

t.penup()
t.seth(360)

for line in range(0, 10):
    t.goto(0, 50*line)
    for i in range(0, 10):
        t.color(random_color())
        t.dot(20)
        t.fd(50)


screen.exitonclick()
