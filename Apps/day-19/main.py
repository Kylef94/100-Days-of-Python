from turtle import Turtle, Screen
screen = Screen()

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Who will win? pick a color")
colors = ["red", "orange", "yellow","green","blue","purple"]

for i in range(0,6):
    t = Turtle(shape="turtle")
    t.color(colors[i])
    t.penup()
    t.goto(x=-230, y=-70+(i*30))

screen.exitonclick()