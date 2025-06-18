# 📝 Python To-Do List com Tkinter (MVC)

Este projeto é uma aplicação de lista de tarefas (To-Do List) desenvolvida em **Python**, utilizando a biblioteca **Tkinter** para a interface gráfica e o padrão arquitetural **MVC (Model-View-Controller)** para uma melhor organização e separação de responsabilidades.

A aplicação permite adicionar, editar, excluir e marcar tarefas com status e prioridade, além de manter persistência dos dados em um arquivo `.json`.

---

## 📌 Funcionalidades

- ✅ **Adicionar tarefas** com definição de prioridade (Alta, Média ou Baixa).
- ✏️ **Editar tarefas**, incluindo o texto e a prioridade. (duplo clique)
- 🗑️ **Excluir tarefas** selecionadas.
- 🟢 **Marcar tarefas como concluídas**, em andamento ou remover a marcação.
- 💾 **Persistência automática** em arquivo `tasks.json`.
- 🎨 **Coloração visual** da tarefa com base no status:
  - Verde: Concluída
  - Amarelo: Em andamento
  - Branco: Pendente

---

## 🧱 Estrutura do Projeto

📦 projeto-todo-list
```
├── controller/
│ └── app_controller.py # Lógica da aplicação (Controller)
├── model/
│ └── task_manager.py # Regras de negócio e persistência (Model)
├── view/
│ └── task_app.py # Interface gráfica (View)
├── tasks.json # Armazenamento persistente das tarefas
├── persistence.py # Módulo utilitário de persistência
└── main.py # Ponto de entrada da aplicação
```



## 🎯 Padrão MVC

- **Model (`model/task_manager.py`)**: Responsável pelas regras de negócio, manipulação da lista de tarefas e persistência em JSON.
- **View (`view/task_app.py`)**: Interface gráfica usando Tkinter. Captura ações do usuário e exibe feedback.
- **Controller (`controller/app_controller.py`)**: Intermedia a comunicação entre a View e o Model.

---

## 🚀 Como executar

### ✅ Requisitos
- Python 3.x
- Tkinter (já incluso na maioria das distribuições Python)

### 🔧 Instalação e execução

1. Clone este repositório:

   ```bash
   git clone https://https://github.com/GabrielJ10/todolist.git
   cd projeto-todo-list
   ```
2.Execute a aplicação:
   ```bash
   python main.py
   ```

---

## 🖼️ Interface Gráfica
A interface é simples, intuitiva e organizada:

- Campo para digitar nova tarefa

- Seleção de prioridade via botões de rádio

- Lista de tarefas com destaque visual por status

- Botões de ação: Adicionar, Editar (duplo clique), Excluir, Marcar como concluída, em andamento ou limpar marcação

---

## 🧪 Exemplo de uso
- Escreva a tarefa no campo de entrada.

- Escolha uma prioridade (Alta, Média ou Baixa).

- Clique em Adicionar.

- Para editar, dê duplo clique em uma tarefa.

- Para excluir, selecione a tarefa e clique em Excluir.

- Use os botões de marcação para controlar o andamento.

## 📂 Persistência

As tarefas são salvas automaticamente no arquivo tasks.json, garantindo que os dados não sejam perdidos ao fechar o programa.