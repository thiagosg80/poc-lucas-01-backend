def get_rbt12(faturamento_periodo: float, quantidade_meses: int) -> float:
    return faturamento_periodo / quantidade_meses * 12 if quantidade_meses < 12 else faturamento_periodo
