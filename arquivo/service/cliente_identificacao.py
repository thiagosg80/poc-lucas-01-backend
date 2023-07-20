from cliente_identificacao.model.identificacao import Identificacao
import re


class ClienteIdentificacaoService:
    def get(self, text: str) -> Identificacao:
        cnpj = self.__get_cnpj(text)
        identificacao = Identificacao()

        if cnpj:
            self.__set_identificacao(identificacao, cnpj, text)

        return identificacao

    def __get_cnpj(self, text: str) -> str:
        match = re.search('N.MERO DE INSCRI..O .{18}', text)

        return self.__get_cnpj_null_safe(match.group()) if match else ''

    def __get_cnpj_null_safe(self, fragment: str):
        start = fragment.rfind(' ') + 1
        end = len(fragment)

        return fragment[start:end]

    def __set_identificacao(self, target: Identificacao, cnpj: str, text: str):
        target.cnpj = cnpj
        target.nome_fantasia = self.__get_nome_fantasia(text)
        target.atividade_principal = self.__get_atividade_principal(text)
        target.data_abertura = self.__get_data_abertura(text)

    def __get_nome_fantasia(self, text: str) -> str:
        match = re.search('NOME DE FANTASIA.+PORTE', text)

        return self.__get_nome_fantasia_null_safe(match.group()) if match else ''

    def __get_nome_fantasia_null_safe(self, fragment: str) -> str:
        start_tag = 'FANTASIA) '
        start = fragment.find(start_tag) + len(start_tag)
        end = fragment.find(' PORTE')

        return fragment[start:end]

    def __get_atividade_principal(self, text: str) -> str:
        start_tag = 'ATIVIDADE ECON.MICA PRINCIPAL '
        end_tag = 'C.DIGO E DESCRI..O DAS ATIVIDADES ECON.MICAS SECUND.RIAS'
        match = re.search(start_tag + '.*' + end_tag, text)

        return self.__get_atividade_principal_null_safe(match.group()) if match else ''

    def __get_atividade_principal_null_safe(self, fragment: str) -> str:
        start = len('ATIVIDADE ECONÔMICA PRINCIPAL ')
        end_tag = 'CÓDIGO E DESCRIÇÃO DAS ATIVIDADES ECONÔMICAS SECUNDÁRIAS'
        end = fragment.find(end_tag)

        return fragment[start:end].strip()

    def __get_data_abertura(self, text: str) -> str:
        start_match = 'DATA DE ABERTURA '
        match = re.search(start_match + '.{10}', text)

        return self.__get_data_abertura_null_safe(match.group(), start_match) if match else ''

    def __get_data_abertura_null_safe(self, fragment, start_match) -> str:
        start = len(start_match)
        end = len(fragment)

        return fragment[start:end]
