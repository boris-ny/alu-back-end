#!/usr/bin/python3

'''Write a Python script that, using this REST API, for a given employee ID, returns information about his/her Todo list progress.'''

import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}' .format(user_id)
    user = requests.get(url).json()
    todo_url = 'https://jsonplaceholder.typicode.com//users/{}/todos/'.format(user_id)
    todo = requests.get(todo_url).json()
    done = []
    for task in todo:
        if task.get('completed') is True:
            done.append(task)
    print('Employee {} is done with tasks({}/{}):' .format(user.get('name'), len(done), len(todo)))
    
    for task in done:
        print('\t {}' .format(task.get('title')))

