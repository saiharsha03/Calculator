import tkinter as tk

from add import add
from sub import sub
from mul import mul
from div import div
from mod import modulo

def calculate(operation):
    firstnumber = float(First_number.get())
    secondnumber = float(Second_number.get())
    result = ""
    y = ""
    if operation == "add":
        result = add(firstnumber, secondnumber)
        y = "+"
    elif operation == "sub":
        result = sub(firstnumber, secondnumber)
        y = "-"
    elif operation == "mul":
        result = mul(firstnumber, secondnumber)
        y = "*"
    elif operation == "div":
        result = div(firstnumber, secondnumber)
        y = "/"
    elif operation == "mod":
        result = modulo(firstnumber, secondnumber)
        y = "%"

    result_label.config(text=f"The result of {firstnumber} {y} {secondnumber} is {result}")

root = tk.Tk()
root.title("Calculator")

First_label = tk.Label(root, text="Enter 1st Number ")
First_label.pack()
First_number = tk.Entry(root)
First_number.pack()

Second_label = tk.Label(root, text="Enter 2nd Number ")
Second_label.pack()
Second_number = tk.Entry(root)
Second_number.pack()

get_add_button = tk.Button(root, text="+", width=50, fg='blue', command=lambda: calculate("add"))
get_add_button.pack()

get_sub_button = tk.Button(root, text="-", width=50, fg='blue', command=lambda: calculate("sub"))
get_sub_button.pack()

get_mul_button = tk.Button(root, text="*", width=50, fg='blue', command=lambda: calculate("mul"))
get_mul_button.pack()

get_div_button = tk.Button(root, text="/", width=50, fg='blue', command=lambda: calculate("div"))
get_div_button.pack()

get_mod_button = tk.Button(root, text="%", width=50, fg='blue', command=lambda: calculate("mod"))
get_mod_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
