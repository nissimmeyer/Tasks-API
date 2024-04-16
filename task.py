from flask import Flask, request
import task_db


app= Flask(__name__)


@app.route('/tasks')
def task_page():
    tasks= task_db.get_all_tasks()
    return tasks

@app.route('/tasks/<int:number>')
def find_specific_task(number: int):
    answer= task_db.get_one_task(number)
    if answer != None:
        return answer
    else:
        return('task not found')
    
@app.route('/tasks', methods= ['POST'])
def add_task():
    new_task = request.json
    task_db.add_task(new_task)
    return new_task

@app.route('/tasks/<int:number>', methods= ['PUT'])
def update_task(number= int):
    task_edit= request.json
    task_db.update_task(number, task_edit)
    return task_edit

@app.route('/tasks/<int:number>', methods= ['DELETE'])
def delete_task(number= int):
    answer= task_db.delete_task(number)
    if answer != None:
        return answer
    else:
        return('task not found')


if __name__== '__main__':
    app.run(port= 5000, host='0.0.0.0', debug= True)

