from flask import Flask, jsonify, request
import json

app = Flask(__name__)

tasks = [
    {
        "id": "0",
        "responsible": "Renan",
        "task": "Making this program work",
        "status": "Pendent"
    }
]

@app.route('/task/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def task_alteration(id):
    if request.method == 'GET':
        try:
            data = tasks[id]
        except IndexError:
            data = {"status":"error", "message":"Index out of range"}
        return jsonify(data)
    elif request.method == 'PUT':
        try:
            data = tasks[id]
            data['status'] = json.loads(request.data)['status']
        except IndexError:
            data = {"status":"error", "message":"Index out of range"}
        return jsonify(data)
    elif request.method == 'DELETE':
        try:
            data = tasks[id]
            tasks.pop(id)
        except IndexError:
            data = {"status":"error", "message":"Index out of range"}
        return jsonify(data)

@app.route('/tasks/', methods=['GET', 'POST'])
def tasks_list():
    if request.method == 'POST':
        task = json.loads(request.data)
        task['id'] = len(tasks)
        tasks.append(task)
        return jsonify(task)
    elif request.method == 'GET':
        return jsonify(tasks)
 

if __name__ == "__main__":
    app.run(debug=True)