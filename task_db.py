import json


def get_all_tasks():
    with open('./tasks-api/tasks_DB.json', 'r') as f:
        tasks= json.load(f)
        return tasks

def get_one_task(number: int):
    with open('./tasks-api/tasks_DB.json', 'r') as f:
        tasks= json.load(f)
        for task in tasks:
            if number != task["number"]:
                continue
            else:
                return task

def add_task(new_task):
    with open('./tasks-api/tasks_DB.json', 'r') as f:
        tasks= json.load(f)
    new_task["number"]= max([task["number"] for task in tasks]) + 1
    tasks.append(new_task)
    with open('./tasks-api/tasks_DB.json', 'w') as f:
        json.dump(tasks, f)
    return new_task

def update_task(number: int, task_edit):
    with open('./tasks-api/tasks_DB.json', 'r') as f:
        tasks= json.load(f)
        for task in tasks:
            if number != task["number"]:
                continue
            else:
                old_task= task        
                task_edit["number"]= old_task["number"]
                tasks.remove(old_task)
                tasks.append(task_edit)
                with open('./tasks-api/tasks_DB.json', 'w') as f:
                    json.dump(tasks, f)
                return task_edit 

def delete_task(number):
    with open('./tasks-api/tasks_DB.json', 'r') as f:
        tasks= json.load(f)
        for task in tasks:
            if number != task["number"]:
                continue
            else:
                tasks.remove(task)
                with open('./tasks-api/tasks_DB.json', 'w') as f:
                    json.dump(tasks, f)
                return 'deleted'
