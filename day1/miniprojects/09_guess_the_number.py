import tkinter as tk
import random

number = random.randint(1, 100)
def guess():
    try:
        g = int(entry.get())
        if g < number:
            label.config(text="Too low!")
        elif g > number:
            label.config(text="Too high!")
        else:
            label.config(text="Correct!")
    except:
        label.config(text="Enter a number.")

def reset():
    global number
    number = random.randint(1, 100)
    label.config(text="Guess a number between 1-100")
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Guess the Number")
label = tk.Label(root, text="Guess a number between 1-100")
label.pack()
entry = tk.Entry(root)
entry.pack()
tk.Button(root, text="Guess", command=guess).pack()
tk.Button(root, text="Reset", command=reset).pack()
root.mainloop()