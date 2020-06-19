from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route('/<int:id>')
def person(id):
    return jsonify({'id': id, 'name':'Renan', 'job':'Developer'})

# @app.route('/sum/<int:value1>/<int:value2>')
# def sum(value1, value2):
#     return jsonify({'soma':value1 + value2})

@app.route('/sum', methods=['POST', 'PUT', 'GET'])
def sum_api():
    if request.method == 'POST':
        data = json.loads(request.data)
        total = sum(data['values'])
    elif request.method == 'GET':
        total = 10 + 10
    return jsonify({'soma': total})

if __name__ == '__main__':
    app.run(debug=True)