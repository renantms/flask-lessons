from flask import Flask, request
from flask_restful import Resource, Api
from abilities import Abilities, Ability
import json
app = Flask(__name__)
api = Api(app)

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

class Developer(Resource):
    def get(self, id):
        try:
            response = developers[id]
        except IndexError:
            message = 'Developer of ID {} doesn\'t exist'.format(id)
            response = {'status':'erro', 'message':message}
        return response
    def put(self, id):
        data = json.loads(request.data)
        developers[id] = data
        return data
    def delete(self, id):
        developers.pop(id)
        return {'status':'success', 'message':'Developer of ID {} got deleted successfully'.format(id)}

class DevelopersList(Resource):
    def get(self):
        return developers
    def post(self):
        data = json.loads(request.data)
        position = len(developers)
        data['id'] = position
        developers.append(data)
        return developers[position]

api.add_resource(Developer, '/dev/<int:id>/')
api.add_resource(DevelopersList, '/dev/')

api.add_resource(Ability, '/ability/<int:id>/')
api.add_resource(Abilities, '/abilities/')

if __name__ == "__main__":
    app.run(debug=True)