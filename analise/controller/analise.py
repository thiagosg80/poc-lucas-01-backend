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
        valor_medio_credito_pis = args.get('valor-medio-credito-pis')
        valor_medio_credito_cofins = args.get('valor-medio-credito-cofins')
        lucro_apurado = args.get('lucro-apurado')
        cnaes = args.get('cnaes')
        periodo_inicio = args.get('periodo-inicio')
        periodo_fim = args.get('periodo-fim')

        return AnaliseService().get(faturamento_periodo, salarios_valor, pro_labore_valor, valor_medio_credito_icms,
                                    valor_medio_credito_pis, valor_medio_credito_cofins, lucro_apurado, cnaes,
                                    periodo_inicio, periodo_fim)
