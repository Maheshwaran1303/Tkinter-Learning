import tkinter as tk

def submit():
    summary = f"Name: {name.get()}\nAge: {age.get()}\nColor: {color.get()}"
    result_label.config(text=summary)

root = tk.Tk()

root.title("Survey")

tk.Label(root, text="Name:").pack()
name = tk.Entry(root)
name.pack()

tk.Label(root, text="Age:").pack()
age = tk.Entry(root)
age.pack()

tk.Label(root, text="Favorite Color:").pack()
color = tk.Entry(root)
color.pack()

tk.Button(root, text="Submit", command=submit).pack()
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()