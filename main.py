import random

from snake import Snake
from turtle import Screen
from food import Food
import time
from scoreboard import Score
screen=Screen()
screen.listen()
screen.tracer(0)
score=Score()
food=Food()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Rohan\'s snake game")
snake=Snake()
game_on=True
screen.onkeypress(snake.up,"Up")
screen.onkeypress(snake.down,"Down")
screen.onkeypress(snake.left,"Left")
screen.onkeypress(snake.right,"Right")
while game_on:
    screen.update()
    time.sleep(0.05)
    snake.move()
    if snake.head.distance(food) < 25:
        food.refresh()
        score.increase_score()
        snake.extend()
    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()>290 or snake.head.ycor()<-290:
        score.alert()
        game_on=False
    for i in snake.snakebody:
        if i==snake.head:
            pass
        else:
            if snake.head.distance(i)<10:
                score.alert()
                game_on=False
screen.exitonclick()