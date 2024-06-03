#!/usr/bin/python3
"""Gets an employee's TODO list progress from an API"""

import requests
import sys

if __name__ == "__main__":
    id = sys.argv[1]

    api = "https://jsonplaceholder.typicode.com"
    template = "Employee {} is done with tasks({}/{}):"
    emp_endpoint = f"{api}/users/{id}"
    todo_endpoint = f"{emp_endpoint}/todos"

    employee = requests.get(emp_endpoint).json()
    todos = requests.get(todo_endpoint).json()
    completed = [task for task in todos if task.get("completed")]
    print(template.format(employee.get("name"), len(completed), len(todos)))
    for todo in completed:
        print(f"\t {todo.get('title')}")
