from flask_restful import Resource
from modelo.service.modelo import ModeloService


class ModeloTreinamentoController(Resource):
    def get(self):
        modelo_service = ModeloService()
        return {'accuracy': modelo_service.fit()}
