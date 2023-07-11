from analise.enum.percentual_common import PercentualCommon


def get_icms(faturamento_periodo: float, valor_medio_credito_icms: float) -> float:
    return faturamento_periodo * PercentualCommon.ICMS.value - valor_medio_credito_icms
