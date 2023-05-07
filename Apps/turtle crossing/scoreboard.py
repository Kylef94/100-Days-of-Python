from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.keepscore()


    def game_over(self):
        self.home()
        msg.write('Game over', align= 'center', font=FONT)

    def keepscore(self):
        self.clear()
        self.goto(-230, 260)
        self.write(f'Level {self.level}', align= 'center', font=FONT)

    def levelup(self):
        self.level += 1
        self.keepscore()