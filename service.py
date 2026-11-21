from datetime import datetime 
from storage import load_tasks, save_tasks 


def add_task(description: str) -> dict:
    if description is None or not description.strip(): 
        raise ValueError("Task description cannot be empty.")
    tasks = load_tasks()
    if not tasks:
        next_id = 1
    else:
        highest_id = 0
        for t in tasks:
            if t["id"] > highest_id:
                highest_id = t["id"]
        next_id = highest_id + 1
    now = datetime.now().isoformat()
    new_task = {
        "id": next_id,
        "description": description.strip(),
        "status": "todo",
        "createdAt": now,
        "updatedAt": now,
     }
    tasks.append(new_task)
    save_tasks(tasks)
    return new_task

def list_tasks(status = None) -> list[dict]:
    tasks = load_tasks()
    if status is None:
        return tasks
    if status not in ("todo", "in-progress", "done"):
        raise ValueError("Invalid task status.")
    filtered = []
    for task in tasks:
        if task["status"] == status:
            filtered.append(task)
    return filtered

def update_task(task_id: int, new_description: str) -> dict:
    if  new_description is None or not new_description.strip():
        raise ValueError("Task description cannot be empty.")
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description.strip()
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            return task
    else:
        raise ValueError(f"Task with ID {task_id} not found")


def delete_task(task_id: int) -> None:
    tasks = load_tasks()
    for task in tasks:
        if task["id"]  == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            return 
    else:
        raise ValueError(f"Task with ID: {task_id}")

def mark_task_status(task_id: int, new_status: str) -> dict:
    if not new_status in ("todo", "in-progress", "done"):
        raise ValueError("Invalid task status")
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = new_status
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            return task
    else:
        raise ValueError(f"Task with ID: {task_id} not found")
