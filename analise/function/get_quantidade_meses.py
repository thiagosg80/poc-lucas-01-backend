import math
from datetime import datetime


def get_quantidade_meses(periodo_inicio: datetime, periodo_fim: datetime) -> int:
    quantidade_dias_raw = (periodo_fim - periodo_inicio).days

    return math.ceil(quantidade_dias_raw / 30)
