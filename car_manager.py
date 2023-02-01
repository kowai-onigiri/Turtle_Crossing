from turtle import Turtle, Screen
import random
from car import Car

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
SHAPE = ((-5, 0), (-3, 0), (-3, 5), (3, 5), (3, 0), (5, 0), (5, -4), (3, -4),
         (3, -5), (2, -5), (2, -4), (-2, -4), (-2, -5), (-3, -5), (-3, -4), (-5, -4))


class CarManager(Car):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.hideturtle()
        self.car_speed = STARTING_MOVE_DISTANCE
        self.level_tracker = 0
        self.car_chance = 6

    def create_car(self):
        random_chance = random.randint(1, self.car_chance)
        if random_chance == 1:
            self.all_cars.append(Car())


    def car_move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT


    def increase_car_density(self):
        self.car_chance -= 1
