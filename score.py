from turtle import Turtle


class Score:

    def __init__(self):

        self.turtle = Turtle()
        self.high_score = 0
        self.score = 0
        self.turtle.penup()
        self.turtle.hideturtle()
        self.turtle.setpos(x=0, y=260)
        self.turtle.color("white")


    def display(self):
        self.turtle.clear()
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.turtle.write(f"Score: {self.score} | High Score: {self.high_score}", align="center", font=("Courier", 14, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.display()

    # def game_over(self):
    #     self.turtle.setpos(x=0, y=0)
    #     self.turtle.write(f"GAME OVER! Total score: {SCORE} ", align="center", font=("Courier", 14, "normal"))

    def score_calulator(self):

        self.score += 1
        self.turtle.clear()
        self.display()





