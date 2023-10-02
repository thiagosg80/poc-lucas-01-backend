from cliente_identificacao.model.atividade import Atividade
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
        target.atividades_secundarias = self.__get_atividades_secundarias(text)
        target.data_abertura = self.__get_data_abertura(text)

    def __get_nome_fantasia(self, text: str) -> str:
        match = re.search('NOME DE FANTASIA.+PORTE', text)

        return self.__get_nome_fantasia_null_safe(match.group()) if match else ''

    def __get_nome_fantasia_null_safe(self, fragment: str) -> str:
        start_tag = 'FANTASIA) '
        start = fragment.find(start_tag) + len(start_tag)
        end = fragment.find(' PORTE')

        return fragment[start:end]

    def __get_atividade_principal(self, text: str) -> Atividade:
        start_tag = 'ATIVIDADE ECON.MICA PRINCIPAL '
        end_tag = 'C.DIGO E DESCRI..O DAS ATIVIDADES ECON.MICAS SECUND.RIAS'
        match = re.search(start_tag + '.*' + end_tag, text)

        return self.__get_atividade_principal_null_safe(match.group()) if match else ''

    def __get_atividade_principal_null_safe(self, fragment: str) -> Atividade:
        start = len('ATIVIDADE ECONÔMICA PRINCIPAL ')
        end_tag = 'CÓDIGO E DESCRIÇÃO DAS ATIVIDADES ECONÔMICAS SECUNDÁRIAS'
        end = fragment.find(end_tag)
        line = fragment[start:end].strip()

        return self.__get_atividade_from_text(line)

    def __get_atividades_secundarias(self, text: str) -> []:
        start_tag = 'ATIVIDADES ECON.MICAS SECUND.RIAS '
        end_tag = 'C.DIGO E DESCRI..O DA NATUREZA JURÍDICA'
        match = re.search(start_tag + '.*' + end_tag, text)

        return self.__get_atividades_secundarias_null_safe(match.group()) if match else []

    def __get_atividades_secundarias_null_safe(self, fragment: str) -> []:
        start = len('ATIVIDADES ECONÔMICAS SECUNDÁRIAS ')
        end_tag = 'CÓDIGO E DESCRIÇÃO DA NATUREZA JURÍDICA'
        end = fragment.find(end_tag)
        atividades_secundarias_text = fragment[start:end]

        return self.__get_atividades_secundarias_from_text(atividades_secundarias_text)

    def __get_atividades_secundarias_from_text(self, fragment: str) -> []:
        atividades = []
        atividade_secundaria_from_text = self.__get_atividade_secundaria_from_text(fragment)
        new_start = 0
        while atividade_secundaria_from_text:
            atividades.append(self.__get_atividade_from_text(atividade_secundaria_from_text))
            new_start = new_start + len(atividade_secundaria_from_text)
            new_fragment = fragment[new_start:len(fragment)]
            atividade_secundaria_from_text = self.__get_atividade_secundaria_from_text(new_fragment)

        return atividades

    def __get_atividade_secundaria_from_text(self, fragment: str) -> str:
        match = re.search('[A-z] [0-9]', fragment)
        end_position = fragment.find(match.group()) + 1 if match else len(fragment)
        line = fragment[0:end_position]

        return line

    def __get_atividade_from_text(self, line: str) -> Atividade:
        parts = line.split(' - ')
        atividade = Atividade()
        atividade.cnae = parts[0].strip()
        atividade.descricao = parts[1].strip()

        return atividade

    def __get_data_abertura(self, text: str) -> str:
        start_match = 'DATA DE ABERTURA '
        match = re.search(start_match + '.{10}', text)

        return self.__get_data_abertura_null_safe(match.group(), start_match) if match else ''

    def __get_data_abertura_null_safe(self, fragment, start_match) -> str:
        start = len(start_match)
        end = len(fragment)

        return fragment[start:end]
