from turtle import  Screen

from food import Food
from scoreboard import Scoreboard
from snake import Snake
import  time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1) # slow down snake a bit

    snake.move()

    # Detect collision with snake and food
    if snake.head.distance(food) < 15:
        snake.extend() #extend snake
        scoreboard.increase_score() #increase player score
        food.refresh() # move the food to a random coordinate

    # Detect Collision with wall, then game-over
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Detect Collision with tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10 :
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()