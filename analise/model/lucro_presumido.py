from analise.model.presuncao import Presuncao


class LucroPresumido:
    presuncao_irpj: Presuncao
    presuncao_csll: Presuncao
    irpj: float
    adicional_irpj: float
    csll: float
    pis: float
    cofins: float
    icms: float
    inss: float
    valor_medio_credito_icms: float
    carga_tributaria_anual: float
    percentual_dos_tributos: float
