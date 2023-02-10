from tkinter import *
from tkinter import messagebox
import pyperclip
import json
from random import *

# ---------------------------- SEARCH ------------------------------- #
def search():
    website = webstie_input.get().lower()

    try:
        with open(file="data.json", mode="r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            pyperclip.copy(password)
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")

        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters)for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers)for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols)for _ in range(randint(2, 4))]

    new_password = password_letters + password_numbers + password_symbols

    shuffle(new_password)

    password = "".join(new_password)

    pyperclip.copy(password)
    password_input.delete(0, END)
    password_input.insert(0, password)




# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    website = webstie_input.get().lower()
    email = email_input.get()
    password = password_input.get()
    new_data = {website: {"email": email, "password": password}}

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                              f"\nPassword: {password} \nIs it ok to save?")

    if is_ok:
        try:
            with open(file="data.json", mode="r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open(file="data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open(file="data.json", mode="w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            webstie_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=0, columnspan=3)

website_label = Label(text="Website : ")
website_label.grid(row=1, column=0)
email_username_label = Label(text="Email/Username : ")
email_username_label.grid(row=2, column=0)
password_label = Label(text="Password : ")
password_label.grid(row=3, column=0)

webstie_input = Entry(width=20)
webstie_input.grid(row=1, column=1)
email_input = Entry(width=36)
email_input.insert(0, "test@test.com")
email_input.grid(row=2, column=1, columnspan=2)
password_input = Entry(width=20)
password_input.grid(row=3, column=1)

search_button = Button(text="Search", width=15, command=search)
search_button.grid(row=1, column=2)
password_generate_button = Button(text="Generate Password", command=generate_password)
password_generate_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=add)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
