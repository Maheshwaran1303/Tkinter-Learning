import tkinter as tk

def cm_to_inch():
    inch = float(cm_entry.get()) / 2.54
    result_label.config(text=f"{inch:.2f} inches")

root = tk.Tk()
root.title("Unit Converter")
tk.Label(root, text="Centimeters:").pack()
cm_entry = tk.Entry(root)
cm_entry.pack()
tk.Button(root, text="Convert to Inches", command=cm_to_inch).pack()
result_label = tk.Label(root, text="")
result_label.pack()
root.mainloop()