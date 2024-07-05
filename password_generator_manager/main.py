from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def gen_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pass_letter = [choice(letters) for _ in range(randint(8, 10))]
    pass_number = [choice(numbers) for _ in range(randint(2, 4))]
    pass_symbol = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = pass_letter + pass_number + pass_symbol

    shuffle(password_list)

    password = "".join(password_list)
    password_output.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pass():
    website = website_entry.get()
    username = username_entry.get()
    password = password_output.get()

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showinfo("Oops", "Please enter all the fields")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\n "
                                                              f"Email: {username}\n Password: {password}\n Is it "
                                                              f"okay to save?")

        if is_ok:
            with open("pass.txt", 'a') as f:
                f.write(f"{website} | {username} | {password}\n")
                website_entry.delete(0, END)
                username_entry.delete(0, END)
                password_output.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50, background='white')

canvas = Canvas(window, width=200, height=200, bg="white", highlightthickness=0)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", bg="white", fg="black")
website_label.grid(column=0, row=1)
website_entry = Entry(width=36, highlightthickness=0, fg='black', bg="white", insertbackground='black')
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)

username_label = Label(text="Email/Username:", bg="white", fg="black")
username_label.grid(column=0, row=2)
username_entry = Entry(width=36, bg="white", fg='black', insertbackground='black', highlightthickness=0)
username_entry.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password:", bg="white", fg="black")
password_label.grid(column=0, row=3)
password_output = Entry(bg="white", fg="black", width=21, highlightthickness=0, insertbackground='black')
password_output.grid(row=3, column=1)

generate_password_button = Button(text="Generate Password", width=11, bg="white", fg="black", highlightthickness=0,
                                  highlightbackground='white', command=gen_pass)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", bg="white", fg="black", width=34, highlightbackground='white', command=save_pass)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
