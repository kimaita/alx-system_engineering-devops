#!/usr/bin/python3
"""Exports as json information about an employee's TODO list progress,
 given their employee ID
"""

import json
import requests
import sys


if __name__ == "__main__":

    empId = sys.argv[1]

    endpoint = "https://jsonplaceholder.typicode.com"

    emp_resp = requests.get(f"{endpoint}/users/{empId}")
    emp = emp_resp.json()

    todo_resp = requests.get(f"{endpoint}/todos", params={'userId': empId})
    todos = todo_resp.json()

    json_todos = []
    for todo in todos:
        json_todo = {}
        json_todo['task'] = todo.get('title')
        json_todo['completed'] = todo.get('completed')
        json_todo['username'] = emp.get('username')
        json_todos.append(json_todo)

    filename = f"{empId}.json"
    with open(filename, 'w', newline='') as file:
        json.dump({empId: json_todos}, file)
