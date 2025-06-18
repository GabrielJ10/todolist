from model.task_manager import TaskManager

class AppController:
    def __init__(self, view):
        self.model = TaskManager()
        self.view = view
        self.view.set_controller(self)
        self.view.populate(self.model.get_all())

    def add_task(self, text):
        try:
            self.model.add_task(text)
            self.view.populate(self.model.get_all())
            self.view.show_info("Tarefa adicionada com sucesso")

        except ValueError:
            self.view.show_error("Não é permitido tarefa vazia")

    def delete_task(self, index):
        self.model.delete_task(index)
        self.view.populate(self.model.get_all())
        self.view.show_info("Tarefa deletada com sucesso")

    def edit_task(self, index, new_text):
        self.model.edit_task(index, new_text)
        self.view.populate(self.model.get_all())
        self.view.show_info("Tarefa editada com sucesso")
