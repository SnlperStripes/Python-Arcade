from tkinter import *
import pandas
import random
from time import sleep

def quiz_main():
    BACKGROUND_COLOR = "#B1DDC6"
    DATA_ROOT = "quiz_game/data/"
    Language = "French"
    Chosen_word = "trouve"
    Language_tr = "English"



    try:
        data = pandas.read_csv("quiz_game/data/words_to_learn.csv")
        to_learn = data.to_dict(orient="records")

    except FileNotFoundError:
        data = pandas.read_csv("quiz_game/data/french_words.csv")
        to_learn = data.to_dict(orient="records")
        data.to_csv("quiz_game/data/words_to_learn.csv")
        print("Created updating word list")
    else:
        print("Loaded your updated Word list")


    chosen = random.randint(0, 100)

    def pick_number():
        global chosen
        chosen = random.randint(0, 100)

    def new_card():
        global Chosen_word, flip_timer, current_card
        pick_number()

        try:
            window.after_cancel(flip_timer)
        except NameError:
            pass
        current_card = random.choice(to_learn)
        Chosen_word = current_card[Language]
        Chosen_word_tr = current_card[Language_tr]

        new_canvas.itemconfig(canvas_image, image=card_img_f)
        new_canvas.itemconfig(canvas_top_text, text=Language, fill="black")
        new_canvas.itemconfig(canvas_bot_text, text=Chosen_word, fill="black")
        flip_timer = window.after(3000, turn_card)
        

    def turn_card():
        Chosen_word = current_card[Language]
        Chosen_word_tr = current_card[Language_tr]

        new_canvas.itemconfig(canvas_top_text, text=Language_tr, fill="white")
        new_canvas.itemconfig(canvas_bot_text, text=Chosen_word_tr, fill="white")

        new_canvas.itemconfig(canvas_image, image=card_img_b)


    def card_known():
        #to_learn = pandas.read_csv("words_to_learn.csv")

        to_learn.remove(current_card)
        print(len(to_learn))

        df = pandas.DataFrame (to_learn)
        df.to_csv("quiz_game/data/words_to_learn.csv", index=False)

        new_card()

    def card_unknown():
        new_card()

    window = Tk()

    window.title("Flash")
    window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

    flip_timer = window.after(3000, turn_card)

    card_img_f = PhotoImage(file="quiz_game/images/card_front.png")
    card_img_b = PhotoImage(file="quiz_game/images/card_back.png")
    img_right = PhotoImage(file="quiz_game/images/right.png")
    img_wrong = PhotoImage(file="quiz_game/images/wrong.png")

    new_canvas = Canvas(width=800, height=526)
    new_canvas.grid(row=0, column=0, columnspan=2)
    canvas_image = new_canvas.create_image(400, 263, image= card_img_f)
    new_canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
    canvas_top_text = new_canvas.create_text(400, 150, text=Language, anchor="center", font=("Ariel", 40, "italic"))
    canvas_bot_text = new_canvas.create_text(400, 263, text=Chosen_word, anchor="center", font=("Ariel", 60, "bold"))

    unknown_button = Button(image=img_wrong, command=card_unknown)
    unknown_button.grid(row=1, column=0)

    known_button = Button(image=img_right, command=card_known)
    known_button.grid(row=1, column=1)

    new_card()


        
    window.mainloop()