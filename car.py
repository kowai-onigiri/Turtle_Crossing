from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
SHAPE = ((-5, 0), (-3, 0), (-3, 5), (3, 5), (3, 0), (5, 0), (5, -4), (3, -4), (3, -5), (2, -5), (2, -4), (-2, -4), (-2, -5), (-3, -5), (-3, -4), (-5, -4))

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.set_car_shape()
        random_ind = random.randint(0, len(COLORS) - 1)
        self.color(COLORS[random_ind])
        random_y = random.randint(-250, 250)
        self.setposition(x=300, y=random_y)


    def set_car_shape(self):
        self.getscreen().register_shape(name="car", shape=SHAPE)
        self.shape("car")
        self.shapesize(stretch_wid=4, stretch_len=2)
        self.tilt(90)