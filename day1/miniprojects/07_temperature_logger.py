import tkinter as tk

def log_temp():
    temp = entry.get()
    if temp:
        text.insert(tk.END, temp + "\n")
        entry.delete(0, tk.END)

root = tk.Tk()
root.title("Temperature Logger")
entry = tk.Entry(root)
entry.pack()
tk.Button(root, text="Log Temperature", command=log_temp).pack()
text = tk.Text(root, height=8, width=30)
text.pack()
root.mainloop()