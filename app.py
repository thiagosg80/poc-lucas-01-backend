from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from analise.controller.analise import AnaliseController
from arquivo.controller.arquivo import ArquivoController

app = Flask(__name__)
CORS(app)
api = Api(app)


api.add_resource(AnaliseController, '/analises')
api.add_resource(ArquivoController, '/arquivos/upload')

if __name__ == '__main__':
    app.run(debug=True)
