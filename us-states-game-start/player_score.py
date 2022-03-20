from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class PlayerScore(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("score_play.txt", "r") as score_play:
            self.high_score = int(score_play.read())
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}/50", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("score_play.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

