import tkinter as tk
import time

def update_clock():
    now = time.strftime("%H:%M:%S")
    label.config(text=now)
    root.after(1000, update_clock)

root = tk.Tk()

root.title("Digital Clock")
label = tk.Label(root, font=("Arial", 40))
label.pack()

update_clock()

root.mainloop()