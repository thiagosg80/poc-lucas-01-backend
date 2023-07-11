from flask import Response

from analise.model import Input
from analise.service.input import InputService
from analise.service.simples_nacional import SimplesNacionalService


class AnaliseService:
    def get(self, faturamento_periodo, salarios_valor, pro_labore_valor):
        try:
            input_analise = InputService().get(faturamento_periodo, salarios_valor, pro_labore_valor)
            return self.__get(input_analise)
        except ValueError:
            return Response('Bad request', status=400)

    def __get(self, input_analise: Input):
        faturamento_periodo = input_analise.get_faturamento_periodo()
        valor_salarios = input_analise.get_salarios_valor()
        valor_pro_labore = input_analise.get_pro_labore_valor()
        simples_nacional = SimplesNacionalService().get(faturamento_periodo, valor_salarios, valor_pro_labore)

        return {
            'input': {
                'faturamentoPeriodo': faturamento_periodo,
                'valorSalarios': valor_salarios,
                'valorProLabore': valor_pro_labore
            },
            'simplesNacional': {
                'aliquota': simples_nacional.get_aliquota(),
                'aPagarNoPeriodo': simples_nacional.get_a_pagar_no_periodo(),
                'inss': simples_nacional.get_inss(),
                'cargaTributariaAnual': simples_nacional.get_carga_tributaria_anual(),
                'percentualDosTributos': simples_nacional.get_percentual_dos_tributos()
            }
        }
