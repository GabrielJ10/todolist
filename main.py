import tkinter as tk
from view.task_app import TaskApp
from controller.app_controller import AppController

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskApp(root)
    controller = AppController(app)
    root.mainloop()
