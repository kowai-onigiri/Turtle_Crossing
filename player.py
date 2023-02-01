from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
TURTLE_SHAPE = "turtle"
TURTLE_COLOR = "chartreuse"


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(TURTLE_SHAPE)
        self.color(TURTLE_COLOR)
        self.penup()
        self.go_to_start()
        self.setheading(90)
        self.level = 1

    def move(self):
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
