from turtle import Screen
from game import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.10)

    snake.move()
    if snake.head.distance(food) < 20:
        food.refresh()
        score.increase_score()
        snake.extend()
    if snake.end_by_wall() or snake.end_by_tail():
        score.game_over()
        game_is_on = False

screen.exitonclick()
