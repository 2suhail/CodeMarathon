from turtle import Turtle

class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.write(f"Score: {self.score}", align="center", font =("Arial", 21, "normal"))
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font =("Arial", 21, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
