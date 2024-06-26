import time
from turtle import Screen
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.tracer(0)


snake = Snake()
food = Food()
score = Score()



screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")



screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
score.display()

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()

        score.score_calulator()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.reset()
        snake.reset()


    for segments in snake.segments[1:]:
        if snake.head.distance(segments) < 10:
            score.reset()
            snake.reset()




screen.exitonclick()