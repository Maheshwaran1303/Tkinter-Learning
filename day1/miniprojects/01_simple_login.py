import tkinter as tk
from tkinter import messagebox

def login():
    if username.get() == "user" and password.get() == "pass":
        messagebox.showinfo("Login", "Welcome!")
    else:
        messagebox.showerror("Login", "Invalid credentials")

root = tk.Tk()

root.title("Login Form")

tk.Label(root, text="Username:").pack()
username = tk.Entry(root)
username.pack()

tk.Label(root, text="Password:").pack()
password = tk.Entry(root, show="*")
password.pack()

tk.Button(root, text="Login", command=login).pack()

root.mainloop()
