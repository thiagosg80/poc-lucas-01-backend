from flask import Response

from analise.model import Input
from analise.service.input import InputService
from analise.service.lucro_presumido import LucroPresumidoService
from analise.service.lucro_real import LucroRealService
from analise.service.simples_nacional import SimplesNacionalService


class AnaliseService:
    def get(self, faturamento_periodo, salarios_valor, pro_labore_valor, valor_medio_credito_icms,
            valor_medio_credito_pis, valor_medio_credito_cofins, lucro_apurado):
        try:
            input_analise = InputService().get(faturamento_periodo, salarios_valor, pro_labore_valor,
                                               valor_medio_credito_icms, valor_medio_credito_pis,
                                               valor_medio_credito_cofins, lucro_apurado)

            return self.__get(input_analise)
        except ValueError:
            return Response('Bad request', status=400)

    def __get(self, input_analise: Input):
        faturamento_periodo = input_analise.faturamento_periodo
        valor_salarios = input_analise.salarios_valor
        valor_pro_labore = input_analise.pro_labore_valor
        simples_nacional = SimplesNacionalService().get(faturamento_periodo, valor_salarios, valor_pro_labore)
        valor_medio_credito_icms = input_analise.valor_medio_credito_icms

        lucro_presumido = LucroPresumidoService().get(faturamento_periodo, valor_salarios, valor_pro_labore,
                                                      valor_medio_credito_icms)

        valor_medio_credito_pis = input_analise.valor_medio_credito_pis
        valor_medio_credito_cofins = input_analise.valor_medio_credito_cofins
        lucro_apurado = input_analise.lucro_apurado

        lucro_real = LucroRealService().get(faturamento_periodo, valor_medio_credito_icms, valor_medio_credito_pis,
                                            valor_medio_credito_cofins, valor_salarios, valor_pro_labore,
                                            lucro_apurado)

        return {
            'input': {
                'faturamentoPeriodo': faturamento_periodo,
                'valorSalarios': valor_salarios,
                'valorProLabore': valor_pro_labore,
                'valorMedioCreditoICMS': valor_medio_credito_icms,
                'valorMedioCreditoPIS': valor_medio_credito_pis,
                'valorMedioCreditoCOFINS': valor_medio_credito_cofins
            },
            'simplesNacional': {
                'aliquota': simples_nacional.aliquota,
                'aPagarNoPeriodo': simples_nacional.a_pagar_no_periodo,
                'inss': simples_nacional.inss,
                'cargaTributariaAnual': simples_nacional.carga_tributaria_anual,
                'percentualDosTributos': simples_nacional.percentual_dos_tributos
            },
            'lucroPresumido': {
                'presuncaoIRPJ': {
                    'aliquota': lucro_presumido.presuncao_irpj.aliquota,
                    'montante': lucro_presumido.presuncao_irpj.montante
                },
                'presuncaoCSLL': {
                    'aliquota': lucro_presumido.presuncao_csll.aliquota,
                    'montante': lucro_presumido.presuncao_csll.montante
                },
                'irpj': lucro_presumido.irpj,
                'adicionalIRPJ': lucro_presumido.adicional_irpj,
                'csll': lucro_presumido.csll,
                'pis': lucro_presumido.pis,
                'cofins': lucro_presumido.cofins,
                'icms': lucro_presumido.icms,
                'inss': lucro_presumido.inss,
                'cargaTributariaAnual': lucro_presumido.carga_tributaria_anual,
                'percentualDosTributos': lucro_presumido.percentual_dos_tributos
            },
            'lucroReal': {
                'apurado': lucro_real.apurado,
                'irpj': lucro_real.irpj,
                'adicionalIRPJ': lucro_real.adicional_irpj,
                'csll': lucro_real.csll,
                'pis': lucro_real.pis,
                'cofins': lucro_real.cofins,
                'icms': lucro_real.icms,
                'inss': lucro_real.inss,
                'cargaTributariaAnual': lucro_real.carga_tributaria_anual,
                'percentualDosTributos': lucro_real.percentual_dos_tributos
            }
        }
