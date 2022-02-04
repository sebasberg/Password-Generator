from tkinter import *
import random, string

root = Tk()
root.title("Password Generator")
root.configure(background="#FFBC80")
root.iconbitmap("lock-icon.ico")
root.geometry("500x600")
root.resizable(0,0)

# generates password based on length and types of characers user decided to include
# more likely to choose lowercase and uppercase than numbers and symbols based on weights
def generate_password(length, include_lowercase, include_uppercase, include_numbers, include_symbols):
    if not include_lowercase and not include_uppercase and not include_numbers and not include_symbols or length == 0:
        return ""
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    numbers = string.digits
    symbols = "!@#$%&/?^*-_+|"
    # initialize included types
    # choices = [1,2,3,4]
    # weights_list = [5, 5, 3, 1]
    choices = []
    weights_list = []
    if include_lowercase:
        choices.append(1)
        weights_list.append(5)
    if include_uppercase:
        choices.append(2)
        weights_list.append(5)
    if include_numbers:
        choices.append(3)
        weights_list.append(3)
    if include_symbols:
        choices.append(4)
        weights_list.append(1)
    # start password building
    temp = []
    for i in range(length):
        type_id = random.choices(choices, weights=weights_list)[0]
        if type_id == 1:
            temp.append(random.choice(lowercase))
        if type_id == 2:
            temp.append(random.choice(uppercase))
        if type_id == 3:
            temp.append(random.choice(numbers))
        if type_id == 4:
            temp.append(random.choice(symbols))
    # extra rules
    # at least 1 symbol character if length > 4 and symbols included
    if length > 4 and include_symbols and  not any(char in "".join(temp) for char in symbols):
        temp.pop()
        temp.append(random.choice(symbols))
    # at least 1 number character if length > 4 and numbers included
    if length > 4 and include_numbers and not any(char in "".join(temp) for char in numbers):
        # don't remove a symbol character
        for i in range(len(temp)):
            if temp[i] not in symbols:
                temp[i] = random.choice(numbers)
    # shuffle password before returning
    random.shuffle(temp)
    return "".join(temp)

def render_password():
    password.set(generate_password(slider.get(), lower_intvar.get(), upper_intvar.get(), numbers_intvar.get(), symbols_intvar.get()))

# unused_var to make the Scale(command=) work
def move_slider(unused_var):
    password_length_stringvar.set(slider.get())
    password.set(generate_password(slider.get(), lower_intvar.get(), upper_intvar.get(), numbers_intvar.get(), symbols_intvar.get()))


title_label = Label(root, text="Password Generator", font=("Verdana", 26, "bold"), bg="#FFBC80", fg="white")
title_label.place(x=53, y=5)

password_length = Label(root, text="Password Length", font=("Verdana", 14, "bold"), bg="#FFBC80", fg="white")
password_length.place(x=154, y=70)

slider = Scale(root, from_=0, to=50, length=250, orient=HORIZONTAL, bg="#FC4F4F", activebackground="#FC4F4F", showvalue=0, bd=0, command=move_slider)
slider.set(12)
slider.place(x=125, y=100)

password_length_stringvar = StringVar()
password_length_num = Label(root, text=slider.get(), bg="#FFBC80", fg="white", font=("Verdana", 20, "bold"), anchor="center", textvariable=password_length_stringvar)
password_length_num.place(x=230, y=120)

lower_intvar = IntVar()
lowercase_check = Checkbutton(root, text="Lowercase", variable=lower_intvar, padx=20, command=render_password)
lowercase_check.select()
#

upper_intvar = IntVar()
uppercase_check = Checkbutton(root, text="Uppercase", variable=upper_intvar, padx=20, command=render_password)
uppercase_check.select()
#

numbers_intvar = IntVar()
numbers_check = Checkbutton(root, text="Numbers", variable=numbers_intvar, padx=20, command=render_password)
#

symbols_intvar = IntVar()
symbols_check = Checkbutton(root, text="Symbols", variable=symbols_intvar, padx=20, command=render_password)
#

generate_button = Button(root, text="Generate", command=render_password)
#

copy_button = Button(root, text="Copy")
#

password = StringVar()
password.set(generate_password(12, 1, 1, 0, 0))
password_label = Label(root, text="password", textvariable=password, width=60)
#


root.mainloop()
