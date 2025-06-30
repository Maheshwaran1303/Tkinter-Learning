import tkinter as tk

def calculate_bmi():
    try:
        h = float(height.get()) / 100
        w = float(weight.get())
        bmi = w / (h * h)
        result_label.config(text=f"BMI: {bmi:.2f}")
    except:
        result_label.config(text="Invalid input")

root = tk.Tk()

root.title("BMI Calculator")

tk.Label(root, text="Height (cm):").pack()
height = tk.Entry(root)
height.pack()

tk.Label(root, text="Weight (kg):").pack()
weight = tk.Entry(root)
weight.pack()

tk.Button(root, text="Calculate", command=calculate_bmi).pack()
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()