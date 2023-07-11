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
        vendas = args.get('vendas')
        compras_mp = args.get('compras-mp')
        despesa_com_folha = args.get('despesa-com-folha')
        outras_despesas = args.get('outras-despesas')
        impostos = args.get('impostos')
        valor_medio_credito_pis = args.get('valor-medio-credito-pis')
        valor_medio_credito_cofins = args.get('valor-medio-credito-cofins')

        return AnaliseService().get(faturamento_periodo, salarios_valor, pro_labore_valor, valor_medio_credito_icms,
                                    vendas, compras_mp, despesa_com_folha, outras_despesas, impostos,
                                    valor_medio_credito_pis, valor_medio_credito_cofins)
