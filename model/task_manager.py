from persistence import load_tasks, save_tasks

class TaskManager:
    def __init__(self):
        self.tasks = load_tasks()

    def add_task(self, text):
        self.tasks.append({"text": text, "completed": False})
        save_tasks(self.tasks)

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            save_tasks(self.tasks)

    def get_all(self):
        return self.tasks
