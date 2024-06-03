#!/usr/bin/python3
"""
Gets an employee's TODO list progress from an API and exports to JSON
"""

import json
import requests
import sys


def write_to_json(emp_id, data):
    """Writes employee todo status to a JSON file

    Filename:USERNAME.json
    Format: { "USER_ID": [
                          {"task": "TASK_TITLE",
                           "completed": TASK_COMPLETED_STATUS,
                           "username": "USERNAME"},
                          ...
                         ]
            }
    """
    filename = f"{emp_id}.json"
    with open(filename, "w") as file:
        json.dump({emp_id: data}, file)


if __name__ == "__main__":
    id = sys.argv[1]

    api = "https://jsonplaceholder.typicode.com"
    emp_endpoint = f"{api}/users/{id}"
    todo_endpoint = f"{emp_endpoint}/todos"

    employee = requests.get(emp_endpoint).json()
    todos = requests.get(todo_endpoint).json()

    todo_dict = []
    for todo in todos:
        dct = {
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": employee.get("username"),
        }
        todo_dict.append(dct)

    emp_id = employee.get("id")

    write_to_json(emp_id, todo_dict)
