#!/usr/bin/python3
"""
Model to make a request to an
API and retrieve data
"""


import json
import requests


if __name__ == "__main__":
    URL = "https://jsonplaceholder.typicode.com/"
    response = requests.get(f"{URL}users")
    all_users = response.json()

    response = requests.get(f"{URL}todos")
    all_todos = response.json()

    user_json = {}
    for user in all_users:
        user_todos = []
        for todos in all_todos:
            if todos['userId'] == user['id']:
                user_todos.append({"username": user['username'],
                                   "task": todos['title'],
                                   "completed": todos['completed']})
        user_json[user['id']] = user_todos

    with open("todo_all_employees.json", 'w') as file:
        json.dump(user_json, file)
