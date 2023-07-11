from flask_restful import Resource
from flask import request

from analise.service.analise import AnaliseService


class AnaliseController(Resource):
    def get(self):
        args = request.args
        faturamento_periodo = args.get('faturamento-periodo')
        salarios_valor = args.get('valor-salarios')
        pro_labore_valor = args.get('valor-pro-labore')
        valor_medio_credito_icms = args.get('valor-medio-credito-icms')

        return AnaliseService().get(faturamento_periodo, salarios_valor, pro_labore_valor, valor_medio_credito_icms)
