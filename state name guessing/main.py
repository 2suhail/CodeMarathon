import pandas
import turtle


def main():
    screen = turtle.Screen()
    screen.title("US Game")
    image = "blank_states_img.gif"
    screen.addshape(image)
    turtle.shape(image)
    data = pandas.read_csv("50_states.csv")
    all_states = data.state.to_list()
    guessed_states = []
    while len(guessed_states) < 50:
            
        answer_state = screen.textinput(title=f"{len(guessed_states)}/50 correct", prompt="Enter state name: ").title()
        if answer_state == "Exit":
            missed_states = []
            for state in all_states:
                if state not in guessed_states:
                    missed_states.append(state)
            new_data = pandas.DataFrame(missed_states)
            new_data.to_csv("states_to_learn.csv")
            break
        if answer_state in all_states:
            guessed_states.append(answer_state)
            t= turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = data[data.state == answer_state]
            t.goto(int(state_data.x), int(state_data.y))
            t.write(answer_state)


    # screen.exitonclick()

if __name__ == '__main__':
    main()