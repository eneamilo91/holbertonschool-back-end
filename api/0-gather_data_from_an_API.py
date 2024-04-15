#!/usr/bin/python3
"""
Model to make a request to an
API and retrieve data
"""


import json
import requests
from sys import argv


if __name__ == "__main__":
    URL = "https://jsonplaceholder.typicode.com/"
    user_id = argv[1]
    response = requests.get(f"{URL}users/{argv[1]}")
    user = response.json()
    user_name = user['name']

    response = requests.get(f"{URL}todos")
    all_todos = response.json()
    user_todos = []
    for todo in all_todos:
        if todo["userId"] == int(argv[1]):
            user_todos.append(todo)
    nr_tasks = len(user_todos)
    completed_tasks = []
    completed_title = []

    for todo in user_todos:
        if todo["completed"] is True:
            completed_tasks.append(todo)
            completed_title.append(todo["title"])

    print(f"Employee {user_name} is done", end="")
    print(f" with tasks({len(completed_tasks)}/{nr_tasks}):")
    for title in completed_title:
        print(f"\t {title}")
