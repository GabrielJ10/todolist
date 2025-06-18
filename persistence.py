import json
import os

FILE_PATH = "tasks.json"

def save_tasks(tasks):
    with open(FILE_PATH, 'w', encoding='utf-8') as f:
        json.dump(tasks, f, indent=4)

def load_tasks():
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)
