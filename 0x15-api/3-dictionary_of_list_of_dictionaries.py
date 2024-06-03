#!/usr/bin/python3
"""
Gets all employee TODO list progress from an API and exports to JSON
"""

import json
import requests


def write_to_json(data):
    """Writes employee todo status to a JSON file

    Filename: todo_all_employees.json
    Format: { "USER_ID": [
                          {"task": "TASK_TITLE",
                           "completed": TASK_COMPLETED_STATUS,
                           "username": "USERNAME"},
                          ...
                         ]
              "USER_ID" : ...
            }
    """
    filename = "todo_all_employees.json"
    with open(filename, "w") as file:
        json.dump(data, file)


def process_todo(todo, emp_lookup):
    """Transform a todo into a dict for writing out"""

    task = {
        "username": emp_lookup[todo.get("userId")],
        "task": todo.get("title"),
        "completed": todo.get("completed"),
    }

    return task


if __name__ == "__main__":
    api = "https://jsonplaceholder.typicode.com"
    emp_endpoint = f"{api}/users"
    todo_endpoint = f"{api}/todos"

    employees = requests.get(emp_endpoint).json()
    todos = requests.get(todo_endpoint).json()
    emp_lookup = {emp.get("id"): emp.get("username") for emp in employees}

    data = {}
    for todo in todos:
        task = process_todo(todo, emp_lookup)
        id = todo.get("userId")
        data.setdefault(id, []).append(task)

    write_to_json(data)
