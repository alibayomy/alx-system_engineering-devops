#!/usr/bin/python3
'''
A Python script to export data in the JSON format.
'''
import json
import requests

if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users"
    us = requests.get(url, verify=False).json()
    unDic = {}
    uDic = {}
    for user in us:
        uid = user.get("id")
        uDic[uid] = []
        unDic[uid] = user.get("username")
    url = "https://jsonplaceholder.typicode.com/todos"
    todo = requests.get(url, verify=False).json()
    [uDic.get(t.get("userId")).append({"task": t.get("title"),
                                       "completed": t.get("completed"),
                                       "username": unDic.get(
                                               t.get("userId"))})
     for t in todo]
    with open("todo_all_employees.json", 'w') as jsf:
        json.dump(uDic, jsf)
