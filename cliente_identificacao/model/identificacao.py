from cliente_identificacao.model.atividade import Atividade


class Identificacao:
    nome_fantasia: str = ''
    cnpj: str = ''
    atividade_principal: Atividade = Atividade()
    atividades_secundarias: [] = []
    data_abertura: str = ''
