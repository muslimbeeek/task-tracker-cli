#!/usr/bin/env python3
import sys
from service import add_task, list_tasks, update_task, delete_task, mark_task_status


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python3 cli.py <command> [arguments]")
        print("Commands: add, update, delete, mark-in-progress, mark-done, list")
        return

    command = sys.argv[1]

    try:
        if command == "add":
            if len(sys.argv) != 3:
                raise ValueError('Usage: python3 cli.py add "<description>"')
            task = add_task(sys.argv[2])
            print(f"Task added successfully (ID: {task['id']})")

        elif command == "list":
            if len(sys.argv) == 2:
                tasks = list_tasks()
            elif len(sys.argv) == 3:
                tasks = list_tasks(sys.argv[2])
            else:
                raise ValueError("Usage: python3 cli.py list [todo|in-progress|done]")

            if not tasks:
                print("No tasks found.")
            else:
                for task in tasks:
                    print(f"[{task['id']}] {task['description']} ({task['status']})")

        elif command == "update":
            if len(sys.argv) != 4:
                raise ValueError('Usage: python3 cli.py update <id> "<description>"')
            task_id = int(sys.argv[2])
            task = update_task(task_id, sys.argv[3])
            print(f"Task {task['id']} updated successfully.")

        elif command == "delete":
            if len(sys.argv) != 3:
                raise ValueError("Usage: python3 cli.py delete <id>")
            task_id = int(sys.argv[2])
            delete_task(task_id)
            print(f"Task {task_id} deleted successfully.")

        elif command == "mark-in-progress":
            if len(sys.argv) != 3:
                raise ValueError("Usage: python3 cli.py mark-in-progress <id>")
            task_id = int(sys.argv[2])
            task = mark_task_status(task_id, "in-progress")
            print(f"Task {task['id']} marked as in-progress.")

        elif command == "mark-done":
            if len(sys.argv) != 3:
                raise ValueError("Usage: python3 cli.py mark-done <id>")
            task_id = int(sys.argv[2])
            task = mark_task_status(task_id, "done")
            print(f"Task {task['id']} marked as done.")

        else:
            raise ValueError(f"Unknown command: '{command}'")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()