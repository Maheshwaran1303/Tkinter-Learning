import tkinter as tk

questions = [("Capital of France?", "Paris"), ("2+2?", "4"), ("Color of sky?", "Blue")]
q_index = [0]

def check_answer():
    answer = entry.get()
    if answer.strip().lower() == questions[q_index[0]][1].lower():
        result_label.config(text="Correct!")
    else:
        result_label.config(text="Wrong!")
        
def next_question():
    q_index[0] = (q_index[0] + 1) % len(questions)
    label.config(text=questions[q_index[0]][0])
    entry.delete(0, tk.END)
    result_label.config(text="")

root = tk.Tk()

root.title("Quiz App")
label = tk.Label(root, text=questions[0][0])
label.pack()

entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Submit", command=check_answer).pack()
tk.Button(root, text="Next", command=next_question).pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()