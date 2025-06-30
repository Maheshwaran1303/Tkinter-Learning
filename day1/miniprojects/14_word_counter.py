import tkinter as tk

def count_words():
    text_str = text.get("1.0", tk.END)
    words = len(text_str.split())
    label.config(text=f"Words: {words}")

root = tk.Tk()
root.title("Word Counter")
text = tk.Text(root, height=8, width=40)
text.pack()
tk.Button(root, text="Count Words", command=count_words).pack()
label = tk.Label(root, text="Words: 0")
label.pack()
root.mainloop()