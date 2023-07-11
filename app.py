from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from analise.controller.analise import AnaliseController

app = Flask(__name__)
CORS(app)
api = Api(app)


api.add_resource(AnaliseController, '/analises')

if __name__ == '__main__':
    app.run(debug=True)
