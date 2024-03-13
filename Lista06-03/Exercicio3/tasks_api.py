from flask import Flask, request, jsonify
import json

app = Flask(__name__)

def load_tasks():
    with open('tasks_data.json', 'r') as file:
        return json.load(file)

def save_tasks(tasks):
    with open('tasks_data.json', 'w') as file:
        json.dump(tasks, file)

@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = load_tasks()
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    tasks = load_tasks()
    tasks.append(data)
    save_tasks(tasks)
    return jsonify({'message': 'Tarefa adicionada com sucesso'})

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    tasks = load_tasks()
    tasks[task_id] = data
    save_tasks(tasks)
    return jsonify({'message': 'Tarefa atualizada com sucesso'})

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    tasks = load_tasks()
    del tasks[task_id]
    save_tasks(tasks)
    return jsonify({'message': 'Tarefa excluída com sucesso'})

if __name__ == '__main__':
    app.run(debug=True)
