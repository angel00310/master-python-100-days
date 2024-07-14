from turtle import Turtle
ALIGNEMT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()

    #計分表文字
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score {self.score} High Score {self.high_score}", align=ALIGNEMT, font=FONT)

    #重製分數
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt",mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()


    #更新計分
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()


    # # Detect collision with wall 撞牆機制
    # def gane_over(self):
    #     self.color("white")
    #     self.penup()
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNEMT, font=FONT)