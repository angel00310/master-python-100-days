import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(39, 119, 86), (12, 99, 69), (231, 239, 234), (19, 49, 62), (17, 118, 150), (26, 59, 45), (112, 95, 53), (243, 237, 240), (150, 152, 56), (78, 157, 104), (132, 170, 144), (190, 158, 93), (231, 236, 240), (41, 42, 31), (120, 175, 185), (211, 147, 157), (39, 158, 167), (6, 93, 103), (230, 201, 104), (132, 70, 78), (75, 76, 38), (31, 29, 30), (226, 91, 55), (207, 94, 115), (237, 202, 2), (162, 31, 26), (177, 26, 37), (172, 203, 190), (26, 62, 109)]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)





screen = turtle_module.Screen()
screen.exitonclick()

















# Python turtle graphics
from turtle import Turtle, Screen
    # tim = Turtle()
    # tim.shape("turtle")
    # tim.color("red")
    # tim.forward(100)
    # tim.right(90)


# 畫正方形
    # for _ in range(4):
    #     tim.forward(100)
    #     tim.left(90)
    #
    #
    # screen = Screen()
    # screen.exitonclick()


# 畫虛線 Draw a Dashed Line
    # import turtle as t
    # tim = t.Turtle()
    #
    # for _ in range(15):
    #     tim.forward(10)
    #     tim.penup()
    #     tim.forward(10)
    #     tim.pendown()

# 畫多邊形
    # import turtle as t
    # import random
    #
    # tim = t.Turtle()
    #
    # colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
    #
    # def draw_shape(num_sides):
    #     angle = 360 / num_sides
    #     for _ in range(num_sides):
    #         tim.forward(100)
    #         tim.right(angle)
    #
    # for shape_side_n in range(3, 11):
    #     tim.color(random.choice(colours))
    #     draw_shape(shape_side_n)

# 隨機走路
    # import turtle as t
    # import random
    #
    # tim = t.Turtle()
    #
    # colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
    # directions = [0, 90, 180, 270]
    # tim.pensize(15)
    # tim.speed("fastest")
    #
    # for _ in range(200):
    #     tim.color(random.choice(colours))
    #     tim.forward(30)
    #     tim.setheading(random.choice(directions))


# Tuples = (1, 3, 0) 不可變更數值，也不可增減，如果要變更，可以改型態為list = []
    # import turtle as t
    # import random
    #
    # tim = t.Turtle()
    # t.colormode(255)
    #
    # def random_color():
    #     r = random.randint(0,255)
    #     g = random.randint(0,255)
    #     b = random.randint(0,255)
    #     random_color = (r, g, b)
    #     return random_color
    #
    # directions = [0, 90, 180, 270]
    # tim.pensize(15)
    # tim.speed("fastest")
    #
    #
    # for _ in range(200):
    #     tim.color(random_color())
    #     tim.forward(30)
    #     tim.setheading(random.choice(directions))
    #


# Spirograph (反覆畫圈圈)
    # import turtle as t
    # import random
    #
    # tim = t.Turtle()
    # t.colormode(255)
    #
    # def random_color():
    #     r = random.randint(0, 255)
    #     g = random.randint(0, 255)
    #     b = random.randint(0, 255)
    #     color = (r, g, b)
    #     return color
    #
    # tim.speed("fastest")
    # def draw_spirograph(size_of_gap):
    #     for _ in range(int(360 / size_of_gap)):
    #         tim.color(random_color())
    #         tim.circle(100)
    #         tim.setheading(tim.heading() + size_of_gap)
    #
    #
    # draw_spirograph(5)
    #
    # screen = t.Screen()
    # screen.exitonclick()




# import module function
    # import turtle
    # tim = turtle.Turtle()

    # from turtle import Turtle
    # tim = Turtle()

    # from turtle import *
    # #*代表import turtle的所有功能

# 在import時修改module名稱
    #import turtle as t
    #tim = t.Turtle

