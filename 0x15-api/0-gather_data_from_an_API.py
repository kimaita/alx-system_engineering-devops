#!/usr/bin/python3
"""Returns information about an employee's TODO list progress,
 given their employee ID.
"""

import sys

import requests


if __name__ == "__main__":

    empId = sys.argv[1]

    endpoint = "https://jsonplaceholder.typicode.com"

    emp_resp = requests.get(f"{endpoint}/users/{empId}")
    emp = emp_resp.json()

    todo_resp = requests.get(f"{endpoint}/todos", params={'userId': empId})
    todos = todo_resp.json()
    completed = [todo.get('title') for todo in todos if todo.get('completed')]

    temp = "Employee {0} is done with tasks({1}/{2}):"
    print(temp.format(emp.get('name'), len(completed), len(todos)))
    for todo in completed:
        print('\t', todo)
