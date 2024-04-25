#!/usr/bin/python3
"""Exports as csv information about an employee's TODO list progress,
 given their employee ID
"""

import csv
import requests
import sys


if __name__ == "__main__":

    empId = sys.argv[1]

    endpoint = "https://jsonplaceholder.typicode.com"

    emp_resp = requests.get(f"{endpoint}/users/{empId}")
    emp = emp_resp.json()

    todo_resp = requests.get(f"{endpoint}/todos", params={'userId': empId})
    todos = todo_resp.json()

    for todo in todos:
        todo['userName'] = emp.get('username')

    filename = f"{empId}.csv"
    with open(filename, 'w', newline='') as file:
        fields = ['userId', 'userName', 'completed', 'title']
        writer = csv.DictWriter(file, fields,
                                extrasaction='ignore', quoting=csv.QUOTE_ALL)
        writer.writerows(todos)
