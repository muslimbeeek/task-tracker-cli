import json
from pathlib import Path


task_file = Path.cwd() / "tasks.json"

def load_tasks():
    if not task_file.exists():
        return []
    try:
        with open(task_file, mode="r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return []

def save_tasks(tasks):
    with open(task_file, mode="w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2,)