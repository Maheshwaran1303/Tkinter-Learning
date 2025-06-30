import tkinter as tk

def add_contact():
    contact = f"{name.get()} - {phone.get()}"
    if name.get() and phone.get():
        text.insert(tk.END, contact + "\n")
        name.delete(0, tk.END)
        phone.delete(0, tk.END)

root = tk.Tk()
root.title("Simple Contact Book")
tk.Label(root, text="Name:").pack()
name = tk.Entry(root)
name.pack()
tk.Label(root, text="Phone:").pack()
phone = tk.Entry(root)
phone.pack()
tk.Button(root, text="Add Contact", command=add_contact).pack()
text = tk.Text(root, height=10, width=30)
text.pack()
root.mainloop()