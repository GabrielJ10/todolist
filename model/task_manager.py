from persistence import load_tasks, save_tasks

class TaskManager:
    def __init__(self):
        self.tasks = load_tasks()

    def add_task(self, text, prioridade = "Média"):
        text = text.strip()
        if not text:
            raise ValueError("Tarefa vazia não permitida")
        prioridade = prioridade.strip()
        self.tasks.append({"text": text, "status": "none", "prioridade": prioridade})
        save_tasks(self.tasks)

    def set_status(self, index, status):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["status"] = status  # 'done', 'pending', or 'none'
            save_tasks(self.tasks)

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            save_tasks(self.tasks)

    def edit_task(self, index, new_text):
        new_text = new_text.strip()
        if not new_text:
            raise ValueError("Tarefa não pode ser vazia")
        if 0 <= index < len(self.tasks):
            self.tasks[index]["text"] = new_text
            save_tasks(self.tasks)

    def editar_prioridade(self, index, prioridade):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["prioridade"] = prioridade
            save_tasks(self.tasks)

    def get_all(self):
        return self.tasks
