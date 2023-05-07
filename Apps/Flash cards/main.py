from tkinter import *
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"

#create screen
window = Tk()
window.title('Flash Cards')
window.config(bg=BACKGROUND_COLOR, pady=50, padx=50)
window.grid()

#Pull data from csv
words_df = pd.read_csv('data/french_words.csv')



#adds flash card
canvas= Canvas(width=800, height=526)
card_front_img = PhotoImage(file='images/card_front.png')
canvas.create_image(400, 263, image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_text(400, 150, text='Title', font=('Ariel', 40, 'italic'))
canvas.create_text(400, 263, text='Word', font=('Ariel', 40, 'italic'))
canvas.grid(column=0, row=0, columnspan=2)

#add and place cross and check buttons for right/wrong answers
cross_image = PhotoImage(file='images/wrong.png')
unknown_button = Button(image=cross_image, highlightthickness=0)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file='images/right.png')
known_button = Button(image=check_image, highlightthickness=0)
known_button.grid(row=1, column=1)


window.mainloop()
