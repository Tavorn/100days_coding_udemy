from turtle import Turtle
ALIGNMENT = "left"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.hideturtle()

    def update_scoreboard(self):
        self.goto(-260, 270)
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)
