#!/usr/bin/python3
"""
Gets an employee's TODO list progress from an API and exports to CSV
"""

import csv
import requests
import sys


def write_to_csv(data):
    """Writes employee todos status to a csv file

    Filename: USER_ID.csv
    Format: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
    """
    filename = f"{data.get('user_id')}.csv"
    with open(filename, "w", newline="") as file:
        headers = ["userId", "username", "completed", "title"]
        writer = csv.DictWriter(
            file,
            headers,
            restval=data["username"],
            extrasaction="ignore",
            quoting=csv.QUOTE_ALL,
        )
        writer.writerows(data.get("todos"))


if __name__ == "__main__":
    id = sys.argv[1]

    api = "https://jsonplaceholder.typicode.com"
    template = "Employee {} is done with tasks({}/{}):"
    emp_endpoint = f"{api}/users/{id}"
    todo_endpoint = f"{emp_endpoint}/todos"

    employee = requests.get(emp_endpoint).json()
    todos = requests.get(todo_endpoint).json()

    write_data = {
        "user_id": employee.get("id"),
        "username": employee.get("username"),
        "todos": todos,
    }
    write_to_csv(write_data)
