#!/usr/bin/python3

'''Write a Python script that, using this REST API, for a given employee ID, returns information about his/her Todo list progress.'''

import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}' .format(user_id)
    user = requests.get(url).json()
    todo_url = 'https://jsonplaceholder.typicode.com//users/{}/todos/'\
        .format(user_id)
    todo = requests.get(todo_url).json()
    employee_name = user.get('name')
    total_tasks = list(filter(lanbda x: x.get('completed') is True, todo))
    tasks_completed = len(total_tasks)
    total_number_of_tasks = len(todo)

    print('Employee {} is done with tasks({}/{}):'\
        .format(employee_name, tasks_completed, total_number_of_tasks))
    
    [print('\t' + task["title"]) for task in total_tasks]
