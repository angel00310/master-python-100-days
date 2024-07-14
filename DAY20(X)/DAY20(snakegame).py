import time
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
#關掉動畫


snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    #刷新畫面
    time.sleep(0.1)
    # 延遲1秒
    snake.move()

    #Detect collision with food (探測與食物的碰撞)
    if snake.head.distance(food) < 15:
        food.refresh()
        #延長蛇身
        snake.extend()
        # 計分
        scoreboard.increase_score()

    # Detect collision with wall 撞牆機制
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()



    # Detect collision with tail 撞身機制
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()




    # # 用slice的概念 Detect collision with tail 撞身機制
    # for segment in snake.segments[1:]:
    #     #從list的第二個到最後
    #     if snake.head.distance(segment) < 10:
    #         game_is_on = False
    #         scoreboard.gane_over()















screen.exitonclick()