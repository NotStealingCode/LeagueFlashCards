from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
TITLE_TEXT = ("Ariel", 30, "italic")
WORD_TEXT = ("Ariel", 20, "bold")
current_quote = {}


# NEXT CARD FUNCTION
def next_card():
    global current_quote
    current_quote = random.choice(completed_dataframe)
    canvas.itemconfig(canvas_title, text="Champion Selection Quote", font=TITLE_TEXT)
    canvas.itemconfig(canvas_word, text=current_quote["Quote"], font=WORD_TEXT)
    canvas.itemconfig(canvas_front, image=front_card)


def flip_card():
    global current_quote
    canvas.itemconfig(canvas_title, text="Champion", font=TITLE_TEXT)
    canvas.itemconfig(canvas_word, text=current_quote["Champion"], font=WORD_TEXT)
    canvas.itemconfig(canvas_front, image=back_card)


# DATA
data = pandas.read_csv("./data/league_quotes.csv")
dataframe = pandas.DataFrame(data)
completed_dataframe = dataframe.to_dict(orient="records")

# WINDOW
window = Tk()
window.title("Guess That Champion")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# CANVAS
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card = PhotoImage(file="./images/card_front.png")
back_card = PhotoImage(file="./images/card_back.png")
canvas_front = canvas.create_image(400, 263, image=front_card)
canvas_title = canvas.create_text(400, 150, text="Champion Select Quote", font=TITLE_TEXT)
canvas_word = canvas.create_text(400, 263, text="Word", font=WORD_TEXT)
canvas.grid(column=0, row=0, columnspan=2)

next_card()

# BUTTONS
right_image = PhotoImage(file="./images/right.png")
correct_button = Button(image=right_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card)
correct_button.grid(column=1, row=1)

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=flip_card)
wrong_button.grid(column=0, row=1)

window.mainloop()
