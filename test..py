import tkinter as tk
from tkinter import messagebox
import heapq

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.tasks = []  # Priority queue (min-heap) to store tasks
        self.task_set = set()  # Hash set to avoid duplicate tasks

        # Create GUI widgets
        self.create_widgets()

    def create_widgets(self):
        # Task Entry
        self.task_label = tk.Label(self.root, text="Enter Task:")
        self.task_label.pack(pady=5)

        self.task_entry = tk.Entry(self.root, width=40)
        self.task_entry.pack(pady=5)

        # Priority Entry
        self.priority_label = tk.Label(self.root, text="Enter Priority (lower number = higher priority):")
        self.priority_label.pack(pady=5)

        self.priority_entry = tk.Entry(self.root, width=40)
        self.priority_entry.pack(pady=5)

        # Add Task Button
        self.add_task_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_task_button.pack(pady=10)

        # Task Listbox
        self.tasks_listbox = tk.Listbox(self.root, width=50, height=10)
        self.tasks_listbox.pack(pady=10)

        # Complete Task Button
        self.complete_task_button = tk.Button(self.root, text="Complete Task", command=self.complete_task)
        self.complete_task_button.pack(pady=10)

        # Refresh Button (to update the listbox)
        self.refresh_button = tk.Button(self.root, text="Refresh List", command=self.update_tasks_listbox)
        self.refresh_button.pack(pady=10)

    def add_task(self):
        """Add a task with a given priority."""
        task = self.task_entry.get()
        priority = self.priority_entry.get()

        if not task or not priority:
            messagebox.showwarning("Input Error", "Please enter both a task and a priority.")
            return

        try:
            priority = int(priority)
        except ValueError:
            messagebox.showwarning("Input Error", "Priority must be a number.")
            return

        if task in self.task_set:
            messagebox.showwarning("Duplicate Task", f"Task '{task}' already exists!")
            return

        heapq.heappush(self.tasks, (priority, task))  # Add task to the priority queue
        self.task_set.add(task)  # Add task to the set
        self.update_tasks_listbox()  # Refresh the listbox
        self.task_entry.delete(0, tk.END)  # Clear the task entry
        self.priority_entry.delete(0, tk.END)  # Clear the priority entry

    def complete_task(self):
        """Mark the highest priority task as completed (remove it)."""
        if not self.tasks:
            messagebox.showinfo("No Tasks", "No tasks to complete!")
            return

        priority, task = heapq.heappop(self.tasks)  # Remove the highest priority task
        self.task_set.remove(task)  # Remove the task from the set
        self.update_tasks_listbox()  # Refresh the listbox
        messagebox.showinfo("Task Completed", f"Task '{task}' (Priority {priority}) marked as completed.")

    def update_tasks_listbox(self):
        """Update the Listbox with the current tasks."""
        self.tasks_listbox.delete(0, tk.END)  # Clear the listbox
        for priority, task in sorted(self.tasks):  # Display tasks in priority order
            self.tasks_listbox.insert(tk.END, f"Priority {priority}: {task}")

# Main application
if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()