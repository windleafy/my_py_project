#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""map"""


# @Time    : 2019/10/21 14:08
# @Author  : Wind
# @Des     : 
# @Software: PyCharm

def square(x):
    return x ** 2


tmp = map(square, [1, 2, 3, 4, 5])
for i in tmp:
    print(i)

tmp = map(lambda x: x ** 2, [1, 2, 3, 4, 5])
for i in tmp:
    print(i)

tasks = [
    {
        "description": "Milk, Cheese, Pizza, Fruit, Tylenol",
        "done": False,
        "id": 1,
        "title": "Buy groceries"
    },
    {
        "description": "Need to find a good Python tutorial on the web",
        "done": False,
        "id": 2,
        "title": "Learn Python"
    },
    {
        "description": "",
        "done": False,
        "id": 3,
        "title": "Read a book"
    }
]


# 将原字段"id"，换成新字段"uri"
def make_public_task(task):
    new_task = {}
    for field in task:
        if field == 'id':
            new_task['uri'] = "http://localhost:5000/todo/api/v1.0/tasks/" + str(task["id"])
        else:
            new_task[field] = task[field]
    return new_task


temp = map(make_public_task, tasks)

for i in temp:
    print(i)


