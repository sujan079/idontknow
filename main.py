import tkinter as tk
from tkinter import messagebox
import heapq


class TodoList:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.tasks = []  # Priority queue for tasks
        self.task_set = set()  # Hash set to avoid duplicates

        # UI elements
        self.create_widgets()

    def create_widgets(self):
        # Task entry
        self.task_label = tk.Label(self.root, text="Enter your task:")
        self.task_label.pack(pady=2)

        self.task_entry = tk.Entry(self.root, width=40)
        self.task_entry.pack(pady=2)

        self.priority_label = tk.Label(self.root, text="Enter the priority:")
        self.priority_label.pack(pady=2)

        self.priority_entry = tk.Entry(self.root, width=10)
        self.priority_entry.pack(pady=2)

        # Buttons
        self.add_task_button = tk.Button(
            self.root, text="Add Task", command=self.add_task
        )
        self.add_task_button.pack(pady=10)

        # Task list
        self.task_listbox = tk.Listbox(self.root, width=50, height=10)
        self.task_listbox.pack(pady=10)

        # Complete task button
        self.complete_button = tk.Button(
            self.root, text="Complete Task", command=self.complete_task
        )
        self.complete_button.pack(pady=10)

        # Search functionality
        self.search_label = tk.Label(self.root, text="Search task:")
        self.search_label.pack(pady=2)

        self.search_entry = tk.Entry(self.root, width=40)
        self.search_entry.pack(pady=2)

        self.search_button = tk.Button(
            self.root, text="Search", command=self.search_task
        )
        self.search_button.pack(pady=2)

        # Reset search button
        self.reset_search_button = tk.Button(
            self.root, text="Reset Search", command=self.reset_search
        )
        self.reset_search_button.pack(pady=2)

    def add_task(self):
        task = self.task_entry.get()
        priority = self.priority_entry.get()
        if not task or not priority:
            messagebox.showwarning("Warning", "Task and priority are required")
            return
        if task in self.task_set:
            messagebox.showwarning("Warning", "Task already exists")
            return

        # Add task to the priority queue
        heapq.heappush(self.tasks, (int(priority), task))
        self.task_set.add(task)
        self.update_tasks_listbox()  # Refresh the listbox
        self.task_entry.delete(0, tk.END)
        self.priority_entry.delete(0, tk.END)

    def complete_task(self):
        if not self.tasks:
            messagebox.showwarning("Warning", "No task to complete")
            return

        # Remove the task with the highest priority
        priority, task = heapq.heappop(self.tasks)
        self.task_set.remove(task)  # Remove the task from the set
        self.update_tasks_listbox()  # Refresh the listbox
        messagebox.showinfo(
            "Task Completed", f"Task '{task}' with priority {priority} completed"
        )

    def update_tasks_listbox(self):
        """Update the task listbox"""
        self.task_listbox.delete(0, tk.END)  # Clear the listbox
        for priority, task in self.tasks:
            self.task_listbox.insert(tk.END, f"{task} - {priority}")

    def search_task(self):
        """Search for tasks by name or priority"""
        query = self.search_entry.get().strip().lower()
        if not query:
            messagebox.showwarning("Warning", "Please enter a search query")
            return

        # Clear the listbox
        self.task_listbox.delete(0, tk.END)

        # Search for tasks that match the query
        found_tasks = []
        for priority, task in self.tasks:
            if query in task.lower() or query == str(priority):
                found_tasks.append((priority, task))

        if not found_tasks:
            messagebox.showinfo("Search Result", "No tasks found matching the query")
        else:
            # Display the found tasks
            for priority, task in found_tasks:
                self.task_listbox.insert(tk.END, f"{task} - {priority}")

    def reset_search(self):
        """Reset the search and display all tasks"""
        self.search_entry.delete(0, tk.END)
        self.update_tasks_listbox()


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoList(root)
    root.mainloop()