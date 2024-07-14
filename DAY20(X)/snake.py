from turtle import Screen, Turtle

STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    # 創建蛇
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    #延長蛇身
    def add_segment(self,position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)


    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
            #讓死掉的蛇離開螢幕(300*300)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]


    def extend(self):
        self.add_segment(self.segments[-1].position())



    #移動蛇
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            # (start= 2,stop= 0,step= -1):start =範圍起點座標, stop = 終點座標, step= 每次的差距
            #  因list從0為起點，因此len-1才會是實際上list內的最後一個數
            # eg: a = [1,2,3],len(a)=3
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    #逆時鐘算，東方為0
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)