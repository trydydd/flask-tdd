import os
from flask import Flask, jsonify
from flask_restful import Resource, Api



#instantiate app
app = Flask(__name__)

api = Api(app)

# set configuration
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)

class Ping(Resource):
    def get(self):
        return {
            'status': 'successs',
            'message': 'pong!'
        }


api.add_resource(Ping, '/ping')