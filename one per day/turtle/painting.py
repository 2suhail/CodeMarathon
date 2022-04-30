import turtle as t
import random
def main():
    colour_choice = ["purple", "red", "orange", "gold", "green", "lime", "blue", "brown", "blue"]
    oogway = t.Turtle()
    oogway.speed(10)
    screen = t.Screen()
    oogway.penup()
    oogway.hideturtle()
    oogway.setposition(-300, -300)
    for i in range(13):
        oogway.setposition(-300, -300 + 50*i)
        for j in range(13):
            oogway.speed(5)
            # oogway.pendown()
            oogway.dot(15, random.choice(colour_choice))
            # oogway.penup()
            oogway.forward(30)
    print(screen.screensize())
    screen.exitonclick()
if __name__ == "__main__":
    main()