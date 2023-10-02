from analise.function.date_br_to_datetime import get_datetime
from analise.model.Input import Input
from analise.model.periodo_apuracao import PeriodoApuracao


class InputService:
    def get(self, faturamento_periodo_input, salarios_valor_input, pro_labore_valor_input,
            valor_medio_credito_icms_input, valor_medio_credito_pis_input, valor_medio_credito_cofins_input,
            lucro_apurado_input, cnaes_input, periodo_inicio_input, periodo_fim_input) -> Input:
        try:
            faturamento_periodo = float(faturamento_periodo_input)
            salarios_valor = float(salarios_valor_input)
            pro_labore_valor = float(pro_labore_valor_input)
            values = [faturamento_periodo, pro_labore_valor, cnaes_input, periodo_inicio_input, periodo_fim_input]
            [self.__check_is_zero(value) for value in values]
            input_analise = Input()
            input_analise.faturamento_periodo = faturamento_periodo
            input_analise.salarios_valor = salarios_valor
            input_analise.pro_labore_valor = pro_labore_valor
            input_analise.valor_medio_credito_icms = self.__get_optional(valor_medio_credito_icms_input)
            input_analise.lucro_apurado = float(lucro_apurado_input)
            input_analise.valor_medio_credito_pis = self.__get_optional(valor_medio_credito_pis_input)
            input_analise.valor_medio_credito_cofins = self.__get_optional(valor_medio_credito_cofins_input)
            input_analise.cnaes = cnaes_input
            periodo = PeriodoApuracao()
            periodo.inicio = get_datetime(periodo_inicio_input)
            periodo.fim = get_datetime(periodo_fim_input)
            input_analise.periodo = periodo

            return input_analise

        except ValueError as error:
            raise error
        except TypeError:
            raise ValueError

    def __get_optional(self, value: float) -> float:
        return float(value) if value else 0

    def __check_is_zero(self, value: float):
        if not bool(value):
            raise ValueError
