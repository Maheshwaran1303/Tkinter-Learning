import tkinter as tk

def calculate():
    try:
        result = eval(entry.get())
        label_result.config(text="Result: " + str(result))
    except:
        label_result.config(text="Invalid Input")

root = tk.Tk()

root.title("Calculator")

entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Calculate", command=calculate).pack()
label_result = tk.Label(root, text="Result:")
label_result.pack()

root.mainloop()