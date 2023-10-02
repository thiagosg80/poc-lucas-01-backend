from flask import Response

from analise.function.datetime_to_date_br import get_date_br
from analise.function.get_quantidade_meses import get_quantidade_meses
from analise.function.get_rbt12 import get_rbt12
from analise.model import Input
from analise.model.simples_nacional_encaixe import SimplesNacionalEncaixe
from analise.service.input import InputService
from analise.service.lucro_presumido import LucroPresumidoService
from analise.service.lucro_real import LucroRealService
from analise.service.simples_nacional import SimplesNacionalService


class AnaliseService:
    def get(self, faturamento_periodo, salarios_valor, pro_labore_valor, valor_medio_credito_icms,
            valor_medio_credito_pis, valor_medio_credito_cofins, lucro_apurado, cnaes, periodo_inicio, periodo_fim):
        try:
            input_analise = InputService().get(faturamento_periodo, salarios_valor, pro_labore_valor,
                                               valor_medio_credito_icms, valor_medio_credito_pis,
                                               valor_medio_credito_cofins, lucro_apurado, cnaes, periodo_inicio,
                                               periodo_fim)

            return self.__get(input_analise)
        except ValueError:
            return Response('Bad request', status=400)

    def __get(self, input_analise: Input):
        periodo = input_analise.periodo
        faturamento_periodo = input_analise.faturamento_periodo
        valor_salarios = input_analise.salarios_valor
        valor_pro_labore = input_analise.pro_labore_valor
        cnaes = input_analise.cnaes
        quantidade_meses = get_quantidade_meses(periodo.inicio, periodo.fim)
        rbt12 = get_rbt12(faturamento_periodo, quantidade_meses)

        simples_nacional = SimplesNacionalService().get(faturamento_periodo, valor_salarios, valor_pro_labore, cnaes,
                                                        rbt12)

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
                'valorMedioCreditoCOFINS': valor_medio_credito_cofins,
                'periodo': {
                    'inicio': get_date_br(periodo.inicio),
                    'fim': get_date_br(periodo.fim)
                },
                'quantidadeMeses': quantidade_meses,
                'rbt12': rbt12
            },
            'simplesNacional': {
                'encaixes': list(map(lambda x: self.__get_simples_nacional_encaixes(x), simples_nacional.encaixes)),
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

    def __get_simples_nacional_encaixes(self, encaixe_input: SimplesNacionalEncaixe) -> dict:
        return {
            'cnae': encaixe_input.cnae,
            'atividadeDescricao': encaixe_input.atividade_descricao,
            'anexo': encaixe_input.anexo,
            'faixaDescricao': encaixe_input.faixa_descricao,
            'aliquota': encaixe_input.aliquota,
            'valorADeduzir': encaixe_input.valor_a_deduzir
        }
