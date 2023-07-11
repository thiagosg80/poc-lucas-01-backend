from analise.model.Input import Input


class InputService:
    def get(self, faturamento_periodo_input, salarios_valor_input, pro_labore_valor_input) -> Input:
        try:
            faturamento_periodo = float(faturamento_periodo_input)
            salarios_valor = float(salarios_valor_input)
            pro_labore_valor = float(pro_labore_valor_input)
            self.__check_input(faturamento_periodo, salarios_valor, pro_labore_valor)

            return Input(faturamento_periodo=faturamento_periodo, salarios_valor=salarios_valor,
                         pro_labore_valor=pro_labore_valor)

        except ValueError as error:
            raise error
        except TypeError:
            raise ValueError

    def __check_input(self, faturamento_periodo: float, salarios_valor: float, pro_labore_valor: float):
        if not bool(faturamento_periodo and salarios_valor and pro_labore_valor):
            raise ValueError
