import tkinter as tk

def submit():
    info = (
        f"Name: {name.get()}\n"
        f"Address: {address.get()}\n"
        f"Phone: {phone.get()}"
    )
    result_label.config(text=info)

root = tk.Tk()

root.title("Address Form")

tk.Label(root, text="Name:").pack()
name = tk.Entry(root)
name.pack()

tk.Label(root, text="Address:").pack()
address = tk.Entry(root)
address.pack()

tk.Label(root, text="Phone:").pack()
phone = tk.Entry(root)
phone.pack()

tk.Button(root, text="Submit", command=submit).pack()
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()