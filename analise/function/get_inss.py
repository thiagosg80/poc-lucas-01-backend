from analise.enum.percentual_common import PercentualCommon


def get_inss(salarios_valor: float, pro_labore_valor: float) -> float:
    inss_salarios = salarios_valor * PercentualCommon.INSS_SALARIOS.value
    inss_pro_labore = pro_labore_valor * PercentualCommon.INSS_PRO_LABORE.value

    return inss_salarios + inss_pro_labore
