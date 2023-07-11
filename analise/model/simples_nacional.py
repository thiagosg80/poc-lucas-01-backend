class SimplesNacional:
    __aliquota: float
    __a_pagar_no_periodo: float
    __inss: float
    __carga_tributaria_anual: float
    __percentual_dos_tributos: float

    def get_aliquota(self) -> float:
        return self.__aliquota

    def set_aliquota(self, aliquota: float):
        self.__aliquota = aliquota

    def get_a_pagar_no_periodo(self) -> float:
        return self.__a_pagar_no_periodo

    def set_a_pagar_no_periodo(self, a_pagar_no_periodo: float):
        self.__a_pagar_no_periodo = a_pagar_no_periodo

    def get_inss(self) -> float:
        return self.__inss

    def set_inss(self, inss: float):
        self.__inss = inss

    def get_carga_tributaria_anual(self) -> float:
        return self.__carga_tributaria_anual

    def set_carga_tributaria_anual(self, carga_tributaria_anual: float):
        self.__carga_tributaria_anual = carga_tributaria_anual

    def get_percentual_dos_tributos(self) -> float:
        return self.__percentual_dos_tributos

    def set_percentual_dos_tributos(self, percentual_dos_tributos: float):
        self.__percentual_dos_tributos = percentual_dos_tributos
