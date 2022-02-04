from tkinter import *
import random, string

root = Tk()
root.title("Password Generator")
root.iconbitmap("lock-icon.ico")
root.geometry("500x700")
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
def render_password_slider(unused_var):
    password.set(generate_password(slider.get(), lower_intvar.get(), upper_intvar.get(), numbers_intvar.get(), symbols_intvar.get()))


title_label = Label(root, text="Password Generator")
title_label.pack()

password_length = Label(root, text="Password Length")
password_length.pack()

slider = Scale(root, from_=0, to=50, length=250, orient=HORIZONTAL, command=render_password_slider)
slider.set(12)
slider.pack()

lower_intvar = IntVar()
lowercase_check = Checkbutton(root, text="Lowercase", variable=lower_intvar, command=render_password)
lowercase_check.select()
lowercase_check.pack()

upper_intvar = IntVar()
uppercase_check = Checkbutton(root, text="Uppercase", variable=upper_intvar, command=render_password)
uppercase_check.select()
uppercase_check.pack()

numbers_intvar = IntVar()
numbers_check = Checkbutton(root, text="Numbers", variable=numbers_intvar, command=render_password)
numbers_check.pack()

symbols_intvar = IntVar()
symbols_check = Checkbutton(root, text="Symbols", variable=symbols_intvar, command=render_password)
symbols_check.pack()

generate_button = Button(root, text="Generate", command=render_password)
generate_button.pack()

copy_button = Button(root, text="Copy")
copy_button.pack()

password = StringVar()
password.set(generate_password(12, 1, 1, 0, 0))
password_label = Label(root, text="password", textvariable=password)
password_label.pack()



root.mainloop()
