# Turtle Race
from turtle import Turtle, Screen
import random

is_race_on =False

screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet",prompt="Which will win the race? Enter a color: ")
colors = ["red","orange","yellow","green","blue","purple"]
y_posotion = [-70,-40,-10,20,50,80]
all_turtles = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_posotion[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You're won! The {winning_color} turtle is the winner!")
            else:
                print(f"You're lost! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)





screen.exitonclick()




# event listen
    # from turtle import Turtle, Screen
    # tim = Turtle()
    # screen = Screen()
    #
    # def move_forwards():
    #     tim.forward(10)
    #
    #
    # screen.listen()
    # screen.onkey(key="space",fun=move_forwards)
    # screen.exitonclick()

# Higher Order Function 在function內使用其他的function


# Etch-A-Sketch
    # from turtle import Turtle, Screen
    # tim = Turtle()
    # screen = Screen()
    #
    # def move_forwards():
    #     tim.forward(10)
    #
    # def move_backwards():
    #     tim.backward(10)
    #
    # def turn_left():
    #     new_heading = tim.heading() + 10
    #     tim.setheading(new_heading)
    #
    # def turn_right():
    #     new_heading = tim.heading() - 10
    #     tim.setheading(new_heading)
    #
    # def clear():
    #     tim.clear()
    #     tim.penup()
    #     tim.home()
    #     tim.pendown()
    #
    # screen.listen()
    # screen.onkey(move_forwards,"w")
    # screen.onkey(move_backwards,"s")
    # screen.onkey(turn_left,"a")
    # screen.onkey(turn_right,"d")
    # screen.onkey(clear,"c")
    #
    #
    # screen.exitonclick()


