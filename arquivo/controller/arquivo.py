from PyPDF2 import PdfReader
from flask import request
from flask_restful import Resource

from analise.model.Input import Input
from arquivo.function.get_text import get_text
from arquivo.service.cliente_identificacao import ClienteIdentificacaoService
from arquivo.service.input import InputService
from cliente_identificacao.model.atividade import Atividade
from cliente_identificacao.model.identificacao import Identificacao


class ArquivoController(Resource):
    def post(self):
        request_input = request.files['file']
        reader = PdfReader(request_input)
        text = get_text(reader.pages)
        input_analise = InputService().get(text)
        identificacao = ClienteIdentificacaoService().get(text)

        return {
            'identificacao': self.__get_identificacao(identificacao),
            'input_analise': self.__get_input_analise(input_analise)
        }

    def __get_identificacao(self, identificacao: Identificacao):
        atividades_secundarias = list(map(self.__get_atividade_json, identificacao.atividades_secundarias))

        return {
            'cnpj': identificacao.cnpj,
            'nome_fantasia': identificacao.nome_fantasia,
            'atividade_principal': self.__get_atividade_json(identificacao.atividade_principal),
            'atividades_secundarias': atividades_secundarias,
            'data_abertura': identificacao.data_abertura
        }

    def __get_atividade_json(self, atividade_input: Atividade):
        return {
            'cnae': atividade_input.cnae,
            'descricao': atividade_input.descricao
        }

    def __get_input_analise(self, input_analise: Input):
        return {
            'faturamento_periodo': input_analise.faturamento_periodo,
            'salarios': input_analise.salarios_valor,
            'pro_labores': input_analise.pro_labore_valor,
            'vendas': input_analise.vendas,
            'valor_medio_credito_icms': input_analise.valor_medio_credito_icms,
            'valor_medio_credito_pis': input_analise.valor_medio_credito_pis,
            'valor_medio_credito_cofins': input_analise.valor_medio_credito_cofins,
            'compras_mp': input_analise.compras_mp,
            'despesa_com_folha': input_analise.despesa_com_folha,
            'outras_despesas': input_analise.outras_despesas,
            'impostos': input_analise.impostos,
            'lucro_apurado': input_analise.lucro_apurado
        }
