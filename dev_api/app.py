from flask import Flask, jsonify, request
import json

app = Flask(__name__)

developers = [
    {   
        "id": "0",
        "name": "Renan",
        "abilities":["Python", "Flask"]
    },{
        "id": "1",
        "name": "Thomaz",
        "abilities":["Python", "Django"]
    }
]

# Returns a developer from the ID, can also change or delete developers
@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def developer(id):
    if request.method == 'GET':
        try:
            response = developers[id]
        except IndexError:
            message = 'Developer of ID {} doesn\'t exist'.format(id)
            response = {"status":"error", "message":message}
        except Exception:
            message = 'Unknowm error.'
            response = {"status":"error", "message":message}
        return jsonify(response)
    elif request.method == 'PUT':
        data = json.loads(request.data)
        developers[id] = data
        return jsonify(data)
    elif request.method == 'DELETE':
        developers.pop(id)
        return jsonify({"status": "success", "message": "Register deleted"})

# Returns a list of all developers and permits to register a new developer
@app.route('/dev/', methods=['POST', 'GET'])
def developers_list():
    if request.method == 'POST':
        data = json.loads(request.data)
        position = len(developers)
        data['id'] = position
        developers.append(data)
        return jsonify(developers[position])
    elif request.method == 'GET':
        return jsonify(developers)

if __name__ == '__main__':
    app.run(debug=True)
