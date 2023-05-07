from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
screen= Screen()
screen.setup(width=680, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
food = Food()
scoreboard = Scoreboard()

snake = Snake()
screen.listen()
screen.onkey(snake.u, "Up")
screen.onkey(snake.d, "Down")
screen.onkey(snake.l, "Left")
screen.onkey(snake.r, "Right")
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.25)
    snake.move()
    #collision with food detection
    if snake.head.distance(food) < 15:
        scoreboard.new_point()
        snake.extend()
        food.refresh()

    #detect wall collision
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        snake.reset()
        scoreboard.reset()

    #detect body collision
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:

            scoreboard.reset()



screen.exitonclick()