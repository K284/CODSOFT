import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0,tk.END)

def delete_task():
    selected_task = listbox.curselection()
    if selected_task:
        listbox.delete(selected_task)

# Create the main window
root = tk.Tk()
root.title("ToDo List")

# Entry for adding tasks
entry = tk.Entry(root, width=30)
entry.pack(padx=80)

# Button to add tasks
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

# Listbox to display tasks
listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=30, height=10)
listbox.pack(pady=20)

# Button to delete selected task
delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack()

# Run the main loop
root.mainloop()
