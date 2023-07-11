from flask import Response

from analise.model import Input
from analise.service.input import InputService


class AnaliseService:
    def get(self, faturamento_periodo, salarios_valor, pro_labore_valor):
        try:
            input_analise = InputService().get(faturamento_periodo, salarios_valor, pro_labore_valor)
            return self.__get(input_analise)
        except ValueError:
            return Response('Bad request', status=400)

    def __get(self, input_analise: Input):
        return {
            'input': {
                'faturamentoPeriodo': input_analise.get_faturamento_periodo(),
                'valorSalarios': input_analise.get_salarios_valor(),
                'valorProLabore': input_analise.get_pro_labore_valor()
            }
        }
