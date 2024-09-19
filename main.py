import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("white")
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing")

scoreboard = Scoreboard()
character = Player()
cars = CarManager()


screen.listen()
screen.onkey(character.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move_cars()

    #detect collision with car
    for car in cars.all_cars:
        if car.distance(character) < 20:
            game_is_on = False
            scoreboard.game_over()

    #detect successful crossing
    if character.is_at_finish_line():
        character.go_to_start()
        cars.level_up()
        scoreboard.increase_level()


screen.exitonclick()