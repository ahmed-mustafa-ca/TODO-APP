import tkinter as tk
from tkinter import messagebox


class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Todo List")
        self.root.geometry("400x400")

        # Task list
        self.tasks = []

        # Create GUI
        self.create_widgets()

    def create_widgets(self):
        # Task entry
        self.task_entry = tk.Entry(self.root, width=40)
        self.task_entry.pack(pady=10)

        # Add button
        add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        add_button.pack(pady=5)

        # Task listbox
        self.task_listbox = tk.Listbox(self.root, width=50, height=15, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10)

        # Mark as done button
        done_button = tk.Button(self.root, text="Mark as Done", command=self.mark_done)
        done_button.pack(side=tk.LEFT, padx=20)

        # Delete button
        delete_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        delete_button.pack(side=tk.RIGHT, padx=20)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({"text": task, "done": False})
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def mark_done(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.tasks[index]["done"] = True
            task_text = self.tasks[index]["text"]
            self.task_listbox.delete(index)
            self.task_listbox.insert(index, f"✓ {task_text}")
        else:
            messagebox.showwarning("Warning", "Please select a task to mark as done.")

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.task_listbox.delete(index)
            del self.tasks[index]
        else:
            messagebox.showwarning("Warning", "Please select a task to delete.")


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()