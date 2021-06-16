import tkinter as tk
import pandas as pd
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
curr_card = {}
to_learn = {}
# ---------------------------- READ CSV ---------------------------- #
try:
    data_csv = pd.read_csv(filepath_or_buffer='data/left_to_learn.csv')
except FileNotFoundError:
    data_csv = pd.read_csv(filepath_or_buffer='data/korean_words.csv')

    to_learn = data_csv.to_dict(orient='records')
else:
    to_learn = data_csv.to_dict(orient='records')


# ---------------------------- FUNCTIONS ----------------------------
def next_card():
    global curr_card, flip_timer
    window.after_cancel(flip_timer)
    curr_card = choice(to_learn)
    canvas.itemconfig(card_language, text="Korean", fill="black")
    canvas.itemconfig(card_word, text=curr_card["Korean"], fill="black")
    canvas.itemconfig(canvas_image, image=card_front)
    flip_timer = window.after(3000, func=flip_card)


def function_yes():
    to_learn.remove(curr_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("data/left_to_learn.csv", index=False)
    next_card()


def flip_card():
    canvas.itemconfig(card_language, text="English", fill="white")
    canvas.itemconfig(card_word, text=curr_card["English"], fill="white")
    canvas.itemconfig(canvas_image, image=card_back)


# ---------------------------- WINDOW ---------------------------- #
window = tk.Tk()
window.title("Flash card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)

# ----------------------------CANVAS---------------------------- #
card_front = tk.PhotoImage(file="images/card_front.png")
card_back = tk.PhotoImage(file="images/card_back.png")

canvas = tk.Canvas(width=800, height=525, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(400, 265, image=card_front)
card_language = canvas.create_text(400, 150, font=('Ariel', 40, 'italic'), text="")
card_word = canvas.create_text(400, 263, font=('Ariel', 60, 'bold'), text='')
canvas.pack()

# ---------------------------- BUTTONS ---------------------------- #
yes_img = tk.PhotoImage(file="images/right.png")
no_img = tk.PhotoImage(file="images/wrong.png")
button_yes = tk.Button(image=yes_img, highlightthickness=0, pady=0, padx=0, command=function_yes)
button_no = tk.Button(image=no_img, highlightthickness=0, pady=0, padx=0, command=next_card)

# ---------------------------- GRID ---------------------------- #

canvas.grid(column=0, row=0, columnspan=2)
button_yes.grid(column=0, row=1)
button_no.grid(column=1, row=1)

# ----------------------------Main loop ---------------------------- #

next_card()

window.mainloop()
