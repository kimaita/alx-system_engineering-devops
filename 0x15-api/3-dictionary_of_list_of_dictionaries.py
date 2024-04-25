#!/usr/bin/python3
"""Exports as json information about all employees TODO list progress
"""

import json
import requests


def getEmployeeTasks(emp_id, emp_uname, tasks):
    """Returns a list of tasks from a single employee

    Args:
        emp_id (int): Employee ID
        tasts (list): list of dicts of tasks
    """
    def fmt_task(task):
        ntask = {'username': emp_uname,
                 'task': task['title'],
                 'completed': task['completed']}
        return ntask

    return [fmt_task(task) for task in tasks if task.get('userId') == emp_id]


if __name__ == "__main__":

    endpoint = "https://jsonplaceholder.typicode.com"

    emp_resp = requests.get(f"{endpoint}/users/")
    employees = emp_resp.json()

    todo_resp = requests.get(f"{endpoint}/todos",)
    todos = todo_resp.json()

    json_dict = {}
    for emp in employees:
        emp_id = emp.get('id')
        emp_uname = emp.get('username')
        json_dict[emp_id] = getEmployeeTasks(emp_id, emp_uname, todos)

    filename = "todo_all_employees.json"
    with open(filename, 'w', newline='') as file:
        json.dump(json_dict, file)
