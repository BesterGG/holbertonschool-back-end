#!/usr/bin/python3
"""Script to generete request using a given APIs"""
import json
import requests
from sys import argv


if __name__ == '__main__':
    """Script for task0"""
    user_request = requests.get(
        'http://jsonplaceholder.typicode.com/users/{}'.format(argv[1])).json()
    todos_req = requests.get(
        'http://jsonplaceholder.typicode.com/todos').json()
    dic = {}
    name = str(user_request.get('username'))
    uid = argv[1]
    dic = {"{}".format(int(argv[1])):
           [{"task": task.get('title'),
             "completed": task.get('completed'),
             "username": user_request.get('username')} for task in todos_req]}

    with open(("{}").format(uid), "w", encoding='utf-8') as f:
        json.dump(dic, f)
