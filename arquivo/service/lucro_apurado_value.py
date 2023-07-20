import re


class LucroApuradoValueService:
    def get(self, text: str) -> float:
        receitas = self.__get_receitas(text)
        despesas = self.__get_despesas(text)

        return receitas - despesas

    def __get_receitas(self, text: str) -> float:
        match = re.search('CONTA.*RESULTADO.*RECEITA.*', text)

        return self.__get_receitas_null_safe(match.group()) if match else 0

    def __get_receitas_null_safe(self, param: str) -> float:
        return self.__get_common_null_safe(param, 'CONTAS DE RESULTADO - RECEITAS', 'C')

    def __get_despesas(self, text: str) -> float:
        match = re.search('CONTA.*RESULTADO.*CUSTO.*DESPESA.*', text)

        return self.__get_despesas_null_safe(match.group()) if match else 0

    def __get_despesas_null_safe(self, param: str) -> float:
        return self.__get_common_null_safe(param, 'CONTAS DE RESULTADOS - CUSTOS E DESPESAS', 'D')

    def __get_common_null_safe(self, param: str, flag_header: str, flag_end_value: str) -> float:
        subtext = param[len(flag_header):len(param)]
        end = subtext.find(flag_end_value)
        value = subtext[0:end].replace('.', '').replace(',', '.')

        return float(value)
