from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

def main():
    
    screen = Screen()
    screen.title("Pong Game")
    screen.bgcolor("black")
    screen.setup(width=800, height=600)

    screen.tracer(0)
    # paddle = Turtle("square")
    # paddle.color("white")
    # paddle.shapesize(stretch_wid=5, stretch_len=1)
    # paddle.penup()
    # paddle.goto(x=350, y=0)
    l_paddle = Paddle((-350, 0))
    r_paddle = Paddle((350, 0))
    ball = Ball()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(r_paddle.go_up, "Up")
    screen.onkey(r_paddle.go_down, "Down")
    screen.onkey(l_paddle.go_up, "w")
    screen.onkey(l_paddle.go_down, "s")
    
    game_status = True
    while game_status:
        time.sleep(0.1)
        screen.update()
        ball.move()

        #detect collision with wall
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()
        #detect collision with paddle 
        if (ball.distance(r_paddle) < 50 and ball.xcor() > 340) or (ball.distance(l_paddle) < 50 and ball.xcor() < -340):
            ball.bounce_x()
            ball.bounce_x()
        #detect when right paddle misses
        if ball.xcor() > 300:
            ball.reset_position()
            scoreboard.l_point()
        #detect when left paddle misses
        if ball.xcor() < -300:
            ball.reset_position()
            scoreboard.r_point()


    screen.exitonclick()
if __name__ == "__main__":
    main()