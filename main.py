import time
import turtle
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# ---------- SCREEN CREATION ----------
screen = Screen()


def turtle_crossing():
    # ---------- SCREEN SETUP ----------
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.tracer(0)

    # ---------- PLAYER CREATION ----------
    player = Player()

    # ----------- CAR CREATION ----------
    car_manager = CarManager()

    # ----------- SCOREBOARD CREATION ----------
    scoreboard = Scoreboard()

    # ---------- CONTROLS -----------
    screen.listen()
    screen.onkey(player.move, "space")

    game_is_on = True
    game_loop = 0

    while game_is_on:
        cars_on_road = car_manager.all_cars
        for car in cars_on_road:
            if car.distance(player) < 30:
                game_is_on = False
                player.color("red")
                player.shapesize(stretch_wid=2, stretch_len=1)
                scoreboard.gameover()

        if player.is_at_finish_line():
            player.go_to_start()
            car_manager.level_up()
            if player.level % 3 == 0:
                car_manager.increase_car_density()
            scoreboard.increase_level()

        time.sleep(0.1)
        screen.update()

        car_manager.create_car()
        car_manager.car_move()
        game_loop += 1


play_again = True

while play_again:
    turtle_crossing()
    another_game = turtle.textinput("Turtle Crossing", "Do you want to play again?").lower()
    if another_game == "yes":
        screen.clear()
    else:
        play_again = False

screen.exitonclick()
