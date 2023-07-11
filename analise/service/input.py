from analise.model.Input import Input


class InputService:
    def get(self, faturamento_periodo_input, salarios_valor_input, pro_labore_valor_input,
            valor_medio_credito_icms_input) -> Input:
        try:
            faturamento_periodo = float(faturamento_periodo_input)
            salarios_valor = float(salarios_valor_input)
            pro_labore_valor = float(pro_labore_valor_input)
            valor_medio_credito_icms = float(valor_medio_credito_icms_input) if valor_medio_credito_icms_input else 0
            self.__check_is_zero(faturamento_periodo, salarios_valor, pro_labore_valor)

            return Input(faturamento_periodo=faturamento_periodo, salarios_valor=salarios_valor,
                         pro_labore_valor=pro_labore_valor, valor_medio_credito_icms=valor_medio_credito_icms)

        except ValueError as error:
            raise error
        except TypeError:
            raise ValueError

    def __check_is_zero(self, faturamento_periodo: float, salarios_valor: float, pro_labore_valor: float):
        if not bool(faturamento_periodo and salarios_valor and pro_labore_valor):
            raise ValueError
