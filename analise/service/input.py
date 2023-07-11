from analise.model.Input import Input


class InputService:
    def get(self, faturamento_periodo_input, salarios_valor_input, pro_labore_valor_input,
            valor_medio_credito_icms_input, vendas_input, compras_mp_input, despesa_com_folha_input,
            outras_despesas_input, impostos_input) -> Input:
        try:
            faturamento_periodo = float(faturamento_periodo_input)
            salarios_valor = float(salarios_valor_input)
            pro_labore_valor = float(pro_labore_valor_input)
            vendas = float(vendas_input)
            values = [faturamento_periodo, salarios_valor, pro_labore_valor, vendas]
            [self.__check_is_zero(value) for value in values]
            input_analise = Input()
            input_analise.faturamento_periodo = faturamento_periodo
            input_analise.salarios_valor = salarios_valor
            input_analise.pro_labore_valor = pro_labore_valor
            input_analise.valor_medio_credito_icms = self.__get_optional(valor_medio_credito_icms_input)
            input_analise.vendas = vendas
            input_analise.compras_mp = self.__get_optional(compras_mp_input)
            input_analise.despesa_com_folha = self.__get_optional(despesa_com_folha_input)
            input_analise.outras_despesas = self.__get_optional(outras_despesas_input)
            input_analise.impostos = self.__get_optional(impostos_input)

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
