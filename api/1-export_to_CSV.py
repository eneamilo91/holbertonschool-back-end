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
    user_name = user['username']

    response = requests.get(f"{URL}todos")
    all_todos = response.json()
    user_todos = []
    for todo in all_todos:
        if todo["userId"] == int(argv[1]):
            user_todos.append(todo)

    with open(f"{user_id}.csv", 'w') as csv:
        for i, todo in enumerate(user_todos):
            first = f'"{user_id}","{user_name}",'
            csv.write(f'{first}"{todo["completed"]}","{todo["title"]}"\n')
