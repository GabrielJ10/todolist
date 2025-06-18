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

        self.listbox.bind("<Double-1>", self.handle_edit)

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

    def handle_edit(self, event):
        index = self.listbox.curselection()[0]
        old_text = self.listbox.get(index)

        def save_edit():
            new_text = entry.get().strip()
            if not new_text:
                self.show_error("Tarefa não pode ser vazia")
                return
            self.controller.edit_task(index, new_text)
            edit_win.destroy()

        edit_win = tk.Toplevel(self.root)
        edit_win.title("Editar Tarefa")

        entry = tk.Entry(edit_win, width=40)
        entry.pack(padx=10, pady=10)
        entry.insert(0, old_text)

        btn = tk.Button(edit_win, text="Salvar", command=save_edit)
        btn.pack(pady=5)

    def populate(self, tasks):
        self.listbox.delete(0, tk.END)
        for task in tasks:
            self.listbox.insert(tk.END, task["text"])

    def show_error(self, message):
        messagebox.showerror("Erro", message)

    def show_info(self, message):
        messagebox.showinfo("Info", message)
