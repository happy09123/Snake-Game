from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

def handle_keypress(return_value):
    handle_keypress.result = return_value

handle_keypress.result = None

finished = False
while not finished:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    for segment in snake.segments[1:]:
        # Detect collision with tail.
        if snake.head.distance(segment) < 10:
            snake.stop = True
            scoreboard.game_over()

            screen.onkey(lambda: handle_keypress(True), "a")
            if handle_keypress.result is not None:
                scoreboard.restart()
                snake.restart()

                handle_keypress.result = None
                break

        # Detect collision with wall.
        if segment.xcor() > 290 or segment.xcor() < -290 \
                or segment.ycor() > 290 or segment.ycor() < -290:
            snake.stop = True
            scoreboard.game_over()

            screen.onkey(lambda: handle_keypress(True), "a")
            if handle_keypress.result is not None:
                scoreboard.restart()
                snake.restart()

                handle_keypress.result = None
                break


screen.exitonclick()