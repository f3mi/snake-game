from turtle import  Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
segment_1 = Turtle("square")

screen.exitonclick()