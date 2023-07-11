from analise.model.lucro import Lucro
from analise.model.presuncao import Presuncao


class LucroPresumido(Lucro):
    presuncao_irpj: Presuncao
    presuncao_csll: Presuncao
