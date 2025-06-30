import tkinter as tk

def load_file():
    try:
        with open(entry.get(), "r") as f:
            text.delete("1.0", tk.END)
            text.insert(tk.END, f.read())
    except:
        text.delete("1.0", tk.END)
        text.insert(tk.END, "File not found.")

root = tk.Tk()
root.title("Text File Viewer")
entry = tk.Entry(root)
entry.pack()
tk.Button(root, text="Load File", command=load_file).pack()
text = tk.Text(root, height=15, width=50)
text.pack()
root.mainloop()