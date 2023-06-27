from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from enquadramento.controller.enquadramento import EnquadramentoController
from modelo.controller.modelo_treinamento import ModeloTreinamentoController


app = Flask(__name__)
CORS(app)
api = Api(app)


api.add_resource(EnquadramentoController, '/enquadramentos/enquadrar')
api.add_resource(ModeloTreinamentoController, '/modelos/treinar')


if __name__ == '__main__':
    app.run(debug=True)
