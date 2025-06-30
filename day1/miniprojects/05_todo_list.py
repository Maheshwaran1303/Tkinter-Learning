import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        tasks.insert(tk.END, task)
        entry.delete(0, tk.END)

def delete_task():
    selected = tasks.curselection()
    if selected:
        tasks.delete(selected)

root = tk.Tk()
root.title("To-Do List")
entry = tk.Entry(root)
entry.pack()
tk.Button(root, text="Add Task", command=add_task).pack()
tasks = tk.Listbox(root)
tasks.pack()
tk.Button(root, text="Delete Selected", command=delete_task).pack()
root.mainloop()