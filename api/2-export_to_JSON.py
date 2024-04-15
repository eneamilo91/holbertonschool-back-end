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

    user_custom_todos = []

    for todo in user_todos:
        user_custom_todos.append({
            "task": todo['title'],
            "completed": todo['completed'],
            "username": user_name})

    json_object = {f"{user_id}": user_custom_todos}

    with open(f"{user_id}.json", 'w') as file:
        json.dump(json_object, file)
