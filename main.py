from tkinter import *
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

try:
    df = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    df = pandas.read_csv("./data/french_words.csv")
    data = df.to_dict(orient="records")
else:
    data = df.to_dict(orient="records")

# ---------------------------- Functions ------------------------------- #
def generate_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    try:
        current_card = choice(data)
    except IndexError:
        print("You learned all words!")

    canvas.itemconfig(canvas_img, image=card_front_img)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    flip_timer= window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(canvas_img, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


def pop_item():
    try:
        data.remove(current_card)
    except ValueError:
        print("You learned all words!")
    else:
        print(len(data))
        generate_card()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady= 50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
canvas_img = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

#Buttons
wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=generate_card)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=pop_item)
right_button.grid(row=1, column=1)

generate_card()

window.mainloop()

to_learn = pandas.DataFrame(data)
to_learn.to_csv("./data/words_to_learn.csv", index=False)
