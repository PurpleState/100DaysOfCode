from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json
# ---------------------------- SEARCH PASSWORD ------------------------------- #


def find_password():
    website = site_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            if website in data:
                email = data[website]['email']
                password = data[website]['password']
                messagebox.showinfo(title="Found", message=f"Username: {email}\n"
                                                           f"Password: {password}")
            else:
                messagebox.askokcancel(title="Error", message="No details for the website exists")
    except FileNotFoundError:
        messagebox.askokcancel(title="Error", message="No Data File Found")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = site_entry.get()
    email = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.askok(title="Oops", message="Please don't leave nay fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n"
                                                              f"Email: {email}\n Password: {password}\n"
                                                              f"Is it okay?")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
                    data.update(new_data)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                site_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
tomato_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=tomato_img)
canvas.grid(column=1, row=0)

site_label = Label(text="Website")
site_label.grid(column=0, row=1)

site_entry = Entry(width=21)
site_entry.grid(column=1, row=1, columnspan=1)

search_button= Button(text="Search", width=13, command=find_password)
search_button.grid(column=2, row=1, columnspan=1)

username_label = Label(text="Username/Email")
username_label.grid(column=0, row=2)

username_entry = Entry(width=35)
username_entry.insert(0, "shilpias@amazon.com")
username_entry.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password")
password_label.grid(column=0, row=3)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
