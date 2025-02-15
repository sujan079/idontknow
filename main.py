# installing the necessary module for the projects


import tkinter as tk
from tkinter import messagebox  # pop up  message
import heapq  # for min heap datastructure


# creating the main application window

class TodoApp:
    def __init__(self, root):  # self constructor
        self.root = root
        self.root.title("To-Do list")
        self.tasks = []  # task first are empty
        self.task_set = set()  # hash set to avoid duplicate


# UI elements for create widgets
        self.create_widgets()

    def create_widgets(self):
        # task entry
        # label for name and pady for vertical padding
        self.task_label = tk.Label(self.root, text='Enter your task:')
        self.task_label.pack(pady=10)

        self.task_entry = tk.Entry(self.root, width=40)
        self.task_entry.pack(pady=10)
        self.priority_label = tk.Label(self.root, text='Enter the priority:')

        self.priority_label.pack(pady=10)
        self.priority_entry = tk.Entry(self.root, width=40)

        # button
        self.add_task_button = tk.Button(
            self.root, text="Add task", command=self.add_task)
        self.add_task_button.pack(pady=10)

        # task list
        self.task_listbox = tk.Listbox(self.root, width=50, height=10)
        self.task_listbox.pack(pady=5)

        # complete task button
        self.complete_button = tk.Button(
            self.root, text="Complete task", command=self.complete_task)
        self.complete_button.pack(pady=5)

        self.refresh_button = tk.Button(
            self.root, text="Refresh", command=self.update_tasks_listbox)
        self.refresh_button.pack(pady=5)


    def add_task(self):
        task = self.task_entry.get()
        priority = self.priority_entry.get()
        if not task or not priority:
            messagebox.showwarning("Warning", "Task and priority required")
            return
        if task in self.task_set:
            messagebox.showwarning("Warning", "Task already exists")
            return

# take task and priority,validate inputs and add them to priotiy queue and update the listbox
    # add task to the priority queue
        heapq.heappush(self.tasks, (int(priority), task))
        self.task_set.add(task)
        self.update_tasks_listbox()  # refresh the listbox
        self.task_entry.delete(0, tk.END)
        self.priority_entry.delete(0, tk.END)

    def complete_task(self):
        if not self.tasks:
            messagebox.showwarning("Warning", "No task to complete")
            return
        # remove the taks with highest priority
        priority, task = heapq.heappop(self.tasks)
        self.task_set.remove(task)  # remove the task from the set
        self.update_tasks_listbox()  # refresh the listbox
        messagebox.showinfo(
            "Task completed", f"Task '{task}' with priority {priority} completed")

    def update_tasks_listbox(self):
        """Update the task listbox"""
        self.task_listbox.delete(0, tk.END)  # clear the listbox
        for priority, task in self.tasks:
            self.task_listbox.insert(tk.END, f"{task} - {priority}")


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
