from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Courier", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def end_game(self):
        super().__init__()
        self.color("red")
        self.hideturtle()
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=("Courier", 24, "normal"))
        self.goto(0, -30)
        self.hideturtle()
        self.write(f" Your score is {self.score}", align="center", font=("Courier", 24, "normal"))