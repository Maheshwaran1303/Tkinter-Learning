import tkinter as tk
from tkinter import messagebox

def submit_feedback():
    messagebox.showinfo("Feedback", "Thank you for your feedback!")
    name_entry.delete(0, tk.END)
    feedback_text.delete("1.0", tk.END)

root = tk.Tk()
root.title("Feedback Collector")
tk.Label(root, text="Name:").pack()
name_entry = tk.Entry(root)
name_entry.pack()
tk.Label(root, text="Feedback:").pack()
feedback_text = tk.Text(root, height=5, width=30)
feedback_text.pack()
tk.Button(root, text="Submit", command=submit_feedback).pack()
root.mainloop()