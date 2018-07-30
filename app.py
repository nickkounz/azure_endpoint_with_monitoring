import sys
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Test(Resource):
    def get(self):
        return {'TestResult': 'Success'}

api.add_resource(Test, '/heartbeat')

if __name__ == "__main__":
    try:
        app.run(host='0.0.0.0', port=5000)
    except Exception:
        sys.exit()