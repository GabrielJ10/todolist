import tkinter as tk
from tkinter import messagebox

class TaskApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.controller = None

        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Adicionar", command=self.handle_add)
        self.add_button.pack()

        self.listbox = tk.Listbox(root, width=50)
        self.listbox.pack(pady=10)

        self.delete_button = tk.Button(root, text="Excluir", command=self.handle_delete)
        self.delete_button.pack()

    def set_controller(self, controller):
        self.controller = controller

    def handle_add(self):
        text = self.entry.get()
        self.controller.add_task(text)
        self.entry.delete(0, tk.END)

    def handle_delete(self):
        try:
            index = self.listbox.curselection()[0]
            self.controller.delete_task(index)
        except IndexError:
            self.show_error("Selecione uma tarefa para excluir")

    def populate(self, tasks):
        self.listbox.delete(0, tk.END)
        for task in tasks:
            self.listbox.insert(tk.END, task["text"])

    def show_error(self, message):
        messagebox.showerror("Erro", message)

    def show_info(self, message):
        messagebox.showinfo("Info", message)
