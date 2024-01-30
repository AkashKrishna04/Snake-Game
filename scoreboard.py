from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 14, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=("courier", 30, "normal"))

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()
