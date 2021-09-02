from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVING_DISTANCE = 20
UP, DOWN, LEFT, RIGHT = 90, 270, 180, 0


class Snake:
    def __init__(self):
        self.parts = []
        self.create_snake()
        self.head = self.parts[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        tim = Turtle(shape="square")
        tim.color("white")
        tim.penup()
        tim.goto(position)
        self.parts.append(tim)

    def extend(self):
        self.add_segment(self.parts[-1].position())

    def move(self):
        for i in range(len(self.parts)-1, 0, -1):
            new_x, new_y = self.parts[i-1].xcor(), self.parts[i-1].ycor()
            self.parts[i].goto(new_x, new_y)
        self.parts[0].forward(MOVING_DISTANCE)

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
