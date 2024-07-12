from turtle import Turtle


class Ball(Turtle):

    #創建球
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 3
        self.y_move = 3
        self.move_speed = 0.1
        # 不可為負數，數字越小越快

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    #反彈機制
    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9
        #每次碰撞時速度都會變快


    # 重製球
    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        #重製速度
        self.bounce_x()
        # 反轉位置
