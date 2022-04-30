import turtle as t
import random
def main():
    colour_choice = ["purple", "red", "orange", "gold", "green", "lime", "blue", "brown", "blue"]
    oogway = t.Turtle()
    # direction = 0
    # oogway.pensize(3)
    oogway.speed(10)
    screen = t.Screen()
    for i in range(50):
        # colour = color_set()
        oogway.pencolor(random.choice(colour_choice))
        oogway.circle(100)
        oogway.setheading(10*i)

    screen.exitonclick()


if __name__ == "__main__":
    main()