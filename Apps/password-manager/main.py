from random import choice,randint, shuffle
from tkinter import *
from tkinter import messagebox
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    pass_letters = [choice(letters) for char in range(randint(8, 10))]
    pass_symbols = [choice(symbols) for sym in range(randint(2, 4))]
    pass_numbers = [choice(numbers) for num in range(randint(2, 4))]

    password_list = pass_letters + pass_numbers + pass_symbols
    shuffle(password_list)

    password = "".join(password_list)

    pass_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pass():
    website = website_entry.get()
    email = user_entry.get()
    password = pass_entry.get()
    new_data = {
        website: {
            'email': email,
            'password': password,
        }
    }

    if len(website) == 0 or len(password) == 0 :
        messagebox.showerror(title='Error', message='Please complete all fields')
    else:
            try:
                with open('data.json', 'r') as file:
                    data = json.load(file)
                    data.update(new_data)

            except FileNotFoundError:
                data = new_data
            else:

                with open('data.json', 'w') as file:
                    json.dump(data, file, indent=4)

                    website_entry.delete(0,END)
                    pass_entry.delete(0,END)


def search():

    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
            website = website_entry.get()

    except FileNotFoundError:
        messagebox.showerror(title='Error', message='No results currently saved!')

    else:
        if website in data:
            info = data.get(website)
            email = info['email']
            password = info['password']
            messagebox.showinfo(title=website, message=f'email: {email} \n'
                                                       f'password: {password}')
        else:
            messagebox.showerror(title='Error', message='Result not found')

# ---------------------------- UI SETUP ------------------------------- #



window = Tk()
window.title('Password Manager')
window.minsize(width=200, height=200)
window.config(padx=50, pady=20, bg='white')

canvas = Canvas(width=200, height=200, bg='white', highlightthickness=0)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100,100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text='Website:', bg='white')
website_label.grid(column=0, row=1)

website_entry = Entry(width=21)
website_entry.grid(column=1,row=1)

user_label = Label(text='Email/Username:', bg='white')
user_label.grid(column=0, row=2)

user_entry = Entry(width=21)
user_entry.insert(END, 'k.farrugia94@gmail.com')
user_entry.grid(column=1,row=2)

pass_label = Label(text='Password:', bg='white')
pass_label.grid(column=0, row=3)

pass_entry = Entry(width=21)
pass_entry.grid(column=1, row=3)
pass_gen_button = Button(text='Generate Password', command=generate_password)
pass_gen_button.grid(column=2, row=3)

add_button = Button(text='Add', width=36, command=save_pass)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text='Search', command=search)
search_button.grid(column=2, row=1)
window.mainloop()

