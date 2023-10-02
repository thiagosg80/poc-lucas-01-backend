from atividade.model.faixa import Faixa


class FaixaSimplesNacionalService:
    map: dict = {}
    faixa_key_predicates = []

    def __init__(self):
        self.map = self.__get_map()
        self.faixa_key_predicates = self.__get_faixa_key_predicates()

    def __get_map(self) -> dict:
        return {
            'I': self.__get_faixas([
                self.__get_faixa(.04, 0),
                self.__get_faixa(.073, 5940),
                self.__get_faixa(.095, 13860),
                self.__get_faixa(.107, 22500),
                self.__get_faixa(.143, 87300),
                self.__get_faixa(.19, 378000)
            ]),
            'II': self.__get_faixas([
                self.__get_faixa(.045, 0),
                self.__get_faixa(.078, 5940),
                self.__get_faixa(.10, 13860),
                self.__get_faixa(.112, 22500),
                self.__get_faixa(.147, 85500),
                self.__get_faixa(.30, 720000)
            ]),
            'III': self.__get_faixas([
                self.__get_faixa(.06, 0),
                self.__get_faixa(.112, 9360),
                self.__get_faixa(.135, 17640),
                self.__get_faixa(.16, 35640),
                self.__get_faixa(.21, 125640),
                self.__get_faixa(.33, 648000)
            ]),
            'IV': self.__get_faixas([
                self.__get_faixa(.045, 0),
                self.__get_faixa(.09, 8100),
                self.__get_faixa(.102, 12420),
                self.__get_faixa(.14, 39780),
                self.__get_faixa(.22, 183780),
                self.__get_faixa(.33, 828000)
            ]),
            'V': self.__get_faixas([
                self.__get_faixa(.155, 0),
                self.__get_faixa(.18, 4500),
                self.__get_faixa(.195, 9900),
                self.__get_faixa(.205, 17100),
                self.__get_faixa(.23, 62100),
                self.__get_faixa(.305, 540000)
            ])
        }

    def __get_faixa_key_predicates(self) -> list:
        UM_MILHAO_E_800_MIL = 1000 * 1000 + 800 * 1000
        TRES_MILHOES_E_600_MIL = 3 * 1000 * 1000 + 600 * 1000
        QUATRO_MILHOES_E_800_MIL = 4 * 1000 * 1000 + 800 * 1000

        predicates = [
            {'callback': lambda x: x <= 180 * 1000, 'key': 'ate_180.000'},
            {'callback': lambda x: 180 * 1000 < x <= 360 * 1000, 'key': 'de_180.000,01_a_360.000'},
            {'callback': lambda x: 360 * 1000 < x <= 720 * 1000, 'key': 'de_360.000,01_a_720.000'},
            {'callback': lambda x: 720 * 1000 < x <= UM_MILHAO_E_800_MIL, 'key': 'de_720.000,01_a_1.800.000'},

            {'callback': lambda x: UM_MILHAO_E_800_MIL < x <= TRES_MILHOES_E_600_MIL,
             'key': 'de_1.800.000,01_a_3.600.000'},

            {'callback': lambda x: TRES_MILHOES_E_600_MIL < x <= QUATRO_MILHOES_E_800_MIL,
             'key': 'de_3.600.000,01_a_4.800.000'},
        ]

        return predicates

    def get(self, anexo_input: str, receita_bruta_em_doze_meses_input: float) -> Faixa:
        anexo = self.map[anexo_input]
        faixa_key = self.get_faixa_key(receita_bruta_em_doze_meses_input)
        faixa_filtered = anexo[faixa_key]
        faixa = Faixa()
        faixa.aliquota = faixa_filtered['aliquota']
        faixa.valor_a_deduzir = faixa_filtered['valor_a_deduzir']

        return faixa

    def __get_faixas(self, faixas: list) -> dict:
        return {
            'ate_180.000': faixas[0],
            'de_180.000,01_a_360.000': faixas[1],
            'de_360.000,01_a_720.000': faixas[2],
            'de_720.000,01_a_1.800.000': faixas[3],
            'de_1.800.000,01_a_3.600.000': faixas[4],
            'de_3.600.000,01_a_4.800.000': faixas[5]
        }

    def __get_faixa(self, percentual_input: float, valor_a_deduzir_input: float) -> dict:
        return {
            'aliquota': percentual_input,
            'valor_a_deduzir': valor_a_deduzir_input
        }

    def get_faixa_key(self, receita_bruta_em_12_meses: float) -> str:
        filtered = filter(lambda x: x['callback'](receita_bruta_em_12_meses), self.faixa_key_predicates)

        return list(filtered)[0]['key']
