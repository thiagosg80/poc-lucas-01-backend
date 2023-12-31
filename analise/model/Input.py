from analise.model.periodo_apuracao import PeriodoApuracao


class Input:
    faturamento_periodo: float
    salarios_valor: float
    pro_labore_valor: float
    valor_medio_credito_icms: float
    vendas: float
    compras_mp: float
    despesa_com_folha: float
    outras_despesas: float
    impostos: float
    valor_medio_credito_pis: float
    valor_medio_credito_cofins: float
    lucro_apurado: float
    cnaes: str
    periodo: PeriodoApuracao
