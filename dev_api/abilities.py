from flask import Flask, request
from flask_restful import Resource
import json

abilities_list = ['Python', 'Java', 'Flask', 'PHP', 'Ruby', 'C#']

class Ability(Resource):
    def get(self, id):
        try:
            response = abilities_list[id]
        except IndexError:
            message = "Index Error"
            response = {"status":"failure", "message":message}
        return response
    def put(self, id):
        try:
            response = abilities_list[id]
            response = json.loads(request.data)
            abilities_list[id] = response
        except IndexError:
            message = "Index Error"
            response = {"status":"failure", "message":message}
        return response
    def delete(self, id):
        try:
            response = abilities_list.pop(id)
        except IndexError:
            message = "Index Error"
            response = {"status":"failure", "message":message}
        return response

class Abilities(Resource):
    def get(self):
        return abilities_list
    def post(self):
        data = json.loads(request.data)
        abilities_list.append(data)
        return data
        