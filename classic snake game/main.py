from turtle import Screen
import time
from snake import Snake
from food import Food
from score import scoreboard
def main():

    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)
    snake = Snake()
    food = Food()
    score = scoreboard()
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
    # screen.update()
    game_status = True
    while game_status == True:
        screen.update()
        time.sleep(0.1)
        snake.move()
    #detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard().increase_score()

    #detect collision with walls
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            game_status = False
            scoreboard().game_over()

        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 5:
                game_status = False
                scoreboard().game_over()





    screen.exitonclick()

if __name__ == "__main__":
    main()