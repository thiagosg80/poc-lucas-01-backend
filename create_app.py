from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from analise.controller.analise import AnaliseController
from arquivo.controller.arquivo import ArquivoController


def create_app() -> Flask:
    flask_app = Flask("PocLucas")
    CORS(flask_app)
    api = Api(flask_app)
    api.add_resource(AnaliseController, '/analises')
    api.add_resource(ArquivoController, '/arquivos/upload')

    return flask_app
