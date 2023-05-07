from turtle import Turtle
FONT = ('arial', 14, 'normal')
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        with open('data.txt') as file:
            self.highscore = int(file.read())
        self.score = 0
        self.penup()
        self.hideturtle()
        self.pencolor('white')
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(0, 275)
        self.write(f"Score: {self.score} High score : {self.highscore}", move=False, align='center', font= FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open('data.txt', mode='w') as file:
                file.write(str(self.highscore))
        self.score = 0

    def new_point(self):
        self.score +=1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", move=False, align='center', font= FONT)