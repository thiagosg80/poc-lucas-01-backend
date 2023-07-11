class Input:
    __faturamento_periodo: float
    __salarios_valor: float
    __pro_labore_valor: float

    def __init__(self, faturamento_periodo: float, salarios_valor: float, pro_labore_valor: float):
        self.__faturamento_periodo = faturamento_periodo
        self.__salarios_valor = salarios_valor
        self.__pro_labore_valor = pro_labore_valor

    def get_faturamento_periodo(self) -> float:
        return self.__faturamento_periodo

    def get_salarios_valor(self) -> float:
        return self.__salarios_valor

    def get_pro_labore_valor(self) -> float:
        return self.__pro_labore_valor
