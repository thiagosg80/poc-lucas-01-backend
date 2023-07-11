from analise.enum.percentual_common import PercentualCommon


def get_adicional_irpj(reference: float) -> float:
    corte = 60 * 1000

    return (reference - corte) * PercentualCommon.ADICIONAL_IRPJ.value if reference > corte else 0
