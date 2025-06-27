import tkinter as tk
from tkinter import ttk
from adder import add_numbers, substract_numbers, multiply_numbers, divide_numbers

def calculate():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        op = operator.get()

        if op == "+":
            result = add_numbers(a, b)
        elif op == "-":
            result = substract_numbers(a, b)
        elif op == "*":
            result = multiply_numbers(a, b)
        elif op == "/":
            result = divide_numbers(a, b)
        else:
            result_label.config(text="Invalid operator")
            return
        
        result_label.config(text=f"Result: {result}")
    except ValueError:
        result_label.config(text="Enter valid numbers")

root = tk.Tk()
root.title("Prettier calculator")

mainframe = ttk.Frame(root, padding="10 10 10 10")
mainframe.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

tk.Label(mainframe, text='First number: ').grid(row = 0, column = 0)
entry1 = tk.Entry(mainframe)
entry1.grid(row = 0, column = 1)

tk.Label(mainframe, text='Second number: ').grid(row = 1, column = 0)
entry2 = tk.Entry(mainframe)
entry2.grid(row = 1, column = 1)

tk.Label(mainframe, text='Operator (+, -, *, /):').grid(row = 2, column = 0)
operator = tk.Entry(mainframe)
operator.grid(row = 2, column = 1)

tk.Button(mainframe, text="Calculate", command=calculate).grid(row = 3, column = 0, columnspan=2)

result_label = tk.Label(mainframe, text="Result:")
result_label.grid(row=4, column=0, columnspan=2)

root.mainloop()