import turtle as t
import random
def color_set():
    r = random.randrange(0,256)
    g = random.randrange(0,256)
    b = random.randrange(0,256)
    return (r, g, b)

# def draw_shape(no_of_sides):
#         oogway = t.Turtle()
#         angle = 360 / no_of_sides
#         for j in range(no_of_sides):
#             oogway.forward(100)
#             oogway.right(angle)

def main():
    colour_choice = ["purple", "red", "orange", "gold", "green", "lime", "blue", "brown", "blue"]
    oogway = t.Turtle()
    screen = t.Screen()
    # t.colormode(255)
    direction = (0, 90, 180, 270)
    oogway.pensize(3)
    oogway.speed(10)
    # paces = (10, 15, 20, 25)
    for i in range(2000):
        # colour = color_set()
        oogway.pencolor(random.choice(colour_choice))
        oogway.forward(10)
        oogway.setheading(random.choice(direction))
    screen.exitonclick()
if __name__ == "__main__":
    main()