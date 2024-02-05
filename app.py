from flask import Flask, jsonify, request
from models.task import Task

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify({
        'message': 'API is running!'
    })

tasks = []
task_id_control = 1

#CREATE
@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id_control
    data = request.get_json()
    new_task = Task(id=task_id_control, title=data['title'], description=data.get("description", ""))
    tasks.append(new_task)
    print(tasks)
    return jsonify({
        'message': 'Nova tarefa criada com sucesso'
    })

#READ

#UPDATE

#DELETE


if __name__ == '__main__':
    app.run(debug=True)
