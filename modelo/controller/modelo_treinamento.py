from flask_restful import Resource

from general.time import Time
from modelo.service.modelo import ModeloService


class ModeloTreinamentoController(Resource):
    def get(self):
        modelo_service = ModeloService()
        modelo_service.fit()
        return {'scheduledAt': modelo_service.pendingFitFlags[0]}
