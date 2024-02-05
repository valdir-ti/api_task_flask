from flask import Flask, jsonify, request
from models.task import Task

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify({
        'message': 'API is running!'
    })

tasks = []
global_id = 1

#CREATE
@app.route('/tasks', methods=['POST'])
def create_task():    
    global global_id
    data = request.get_json()
    new_task = Task(id=global_id, title=data['title'], description=data.get("description", ""))
    tasks.append(new_task)
    print(tasks)
    return jsonify({'message': 'Nova tarefa criada com sucesso'})

# READ
@app.route('/tasks', methods=['GET'])
def get_tasks():
    '''
        Option 1
        task_list = []
        for task in tasks:
            task_list.append(task.to_dict())
    '''

    task_list = [task.to_dict() for task in tasks]
    
    output = {
        "tasks": task_list,
        "total_tasks": len(task_list)
    }
    return jsonify(output)

# READ - ID
@app.route('/tasks/<int:id>', methods=['GET'])
def get_task_by_id(id):    
    for t in tasks:
        if t.id == id:
            return jsonify(t.to_dict())
    return jsonify({'message': 'task not found'}, 404)

# UPDATE
@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
    
    if task == None:
        return jsonify({'message': 'task not found'}, 404)
    
    data = request.get_json()
    task.title = data['title']
    task.description = data['description']
    task.completed = data['completed']

    return jsonify({'message': 'Tarefa atualizada com sucesso'})

# DELETE

if __name__ == '__main__':
    app.run(debug=True)
