from tkinter import *
import pandas
from random import *

BACKGROUND_COLOR = "#B1DDC6"

# ----------------------------- FILE OF WORDS ----------------------------- #
try:
    df = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    df = pandas.read_csv("data/french_words.csv")
    dictionary = df.to_dict(orient="records")
else:
    dictionary = df.to_dict(orient="records")

# ----------------------------- COMMANDS ----------------------------- #

word_couple = {}


def generate_word():
    global word_couple
    canvas.itemconfig(card, image=front_card)
    word_couple = choice(dictionary)
    fr_word = word_couple["French"]
    canvas.itemconfig(vocab, text=fr_word)
    canvas.itemconfig(language, text="French")


def show_translation():
    canvas.itemconfig(card, image=back_card)
    canvas.itemconfig(language, text="English")
    en_word = word_couple["English"]
    canvas.itemconfig(vocab, text=en_word)


def is_known():
    dictionary.remove(word_couple)
    generate_word()
    data = pandas.DataFrame(dictionary)
    data.to_csv("data/words_to_learn.csv", index=False)


# -----------------------------UI SETUP----------------------------- #
window = Tk()
window.title("Flash Card")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

# Flash card
canvas = Canvas()
canvas.config(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card = PhotoImage(file="images/card_front.png")
back_card = PhotoImage(file="images/card_back.png")
card = canvas.create_image(400, 263, image=front_card)
canvas.grid(row=0, column=0, columnspan=3)
language = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
vocab = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

# Buttons
c_image = PhotoImage(file="images/right.png")
correct = Button(image=c_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=is_known)
correct.grid(row=1, column=2)
w_image = PhotoImage(file="images/wrong.png")
wrong = Button(image=w_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=generate_word)
wrong.grid(row=1, column=0)
check_answer = Button(text="Show me the answer", highlightthickness=0, bg=BACKGROUND_COLOR, font=("Ariel", 10),
                      command=show_translation)
check_answer.grid(row=1, column=1)

generate_word()

window.mainloop()


