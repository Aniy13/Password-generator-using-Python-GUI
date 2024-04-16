import random
import pyperclip
from tkinter import *
from tkinter.ttk import *

def low():
    entry.delete(0, END)
    length = string1.get()

    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789!@#$%^&*()"
    password = ""

    if var.get() == 1:
        for i in range(0, length):
            password = password + random.choice(lower)
        return password

    elif var.get() == 0:
        for i in range(0, length):
            password = password + random.choice(upper)
        return password

    elif var.get() == 3:
        for i in range(0, length):
            password = password + random.choice(lower+upper+digits)
        return password


def generate():
    pas = low()
    entry.insert(0, pas)


def copy1():
    random_password = entry.get()
    pyperclip.copy(random_password)


root = Tk()
var = IntVar()
string1 = IntVar()

root.title("Random Password Generator")

Random_password = Label(root, text="Password")
Random_password.grid(row=0)
entry = Entry(root)
entry.grid(row=0, column=1)

label = Label(root, text="Length")
label.grid(row=1, column=0)

copy_button = Button(root, text="Copy", command=copy1)
copy_button.grid(row=0, column=2)
generate_button = Button(root, text="Generate", command=generate)
generate_button.grid(row=0, column=3)

radio_low = Radiobutton(root, text="Low", variable=var, value=1)
radio_low.grid(row=1, column=2,)
radio_middle = Radiobutton(root, text="Medium", variable=var, value=0)
radio_middle.grid(row=1, column=3,)
radio_strong = Radiobutton(root, text="Strong", variable=var, value=3)
radio_strong.grid(row=1, column=4,)
combo: Combobox = Combobox(root, textvariable=string1)

combo['values'] = (8, 9, 10, 11, 12, 13, 14, 15, 16,
                   17, 18, 19, 20, 21, 22, 23, 24, 25,
                   26, 27, 28, 29, 30, 31, 32,)
combo.bind('<<ComboboxSelected>>')

combo.grid(row=1, column=1)

root.mainloop()
