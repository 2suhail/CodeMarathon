from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"




def main():
    
    def next_card():
        global current_card, flip_timer
        window.after_cancel(flip_timer)
        canvas.itemconfig(card_background, image=front_img)
        current_card = random.choice(words_to_learn)
        canvas.itemconfig(card_title, text="French", fill="black")
        canvas.itemconfig(card_word, text=current_card["French"], fill="black")
        flip_timer = window.after(3000, func=flip_card)



    def flip_card():
        global current_card
        #current_card = current_card["English"]
        canvas.itemconfig(card_background, image=back_img)
        canvas.itemconfig(card_title, text="English", fill="white")
        canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    
    def word_known():
        global current_card
        words_to_learn.remove(current_card)
        data = pandas.DataFrame(words_to_learn)
        data.to_csv("./data/words_to_learn.csv", index=False)
        next_card()

    try:
        data = pandas.read_csv("data/words_to_learn.csv")
    except FileNotFoundError:
        original_data = pandas.read_csv("data/french_words.csv")
        words_to_learn = original_data.to_dict(orient="records")
    else:
        words_to_learn = data.to_dict(orient="records")

    current_card = {}
   #UI SETUP
    window = Tk()
    window.title("Flashcard App")
    window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
    global flip_timer 
    flip_timer = window.after(3000, func=flip_card)

    canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
    front_img = PhotoImage(file="./images/card_front.png")
    back_img = PhotoImage(file="./images/card_back.png")
    card_background = canvas.create_image(400, 263, image=front_img)
    card_title = canvas.create_text(400, 150, text="Text", font=("Ariel", 40, "italic"))
    card_word = canvas.create_text(400, 263, text="Word", font=("Ariel", 40, "bold"))
    canvas.grid(column=0, row=0, columnspan=2)
#green button
    green_img = PhotoImage(file="./images/right.png")
    green_button = Button(image=green_img, highlightthickness=0, command=word_known)
    green_button.grid(column=1, row=1)
#red button
    red_img = PhotoImage(file="./images/wrong.png")
    red_button = Button(image=red_img, highlightthickness=0, command=next_card)
    red_button.grid(column=0, row=1)
#
    
    next_card()


    window.mainloop()
if __name__ == "__main__":
    main()
