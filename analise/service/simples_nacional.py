from analise.enum.percentual_simples_nacional import PercentualSimplesNacional
from analise.model.simples_nacional import SimplesNacional


class SimplesNacionalService:
    def get(self, faturamento_periodo: float, salarios_valor: float, pro_labore_valor: float) -> SimplesNacional:
        simples_nacional = SimplesNacional()
        simples_nacional.aliquota = PercentualSimplesNacional.ALIQUOTA.value
        a_pagar = round(faturamento_periodo * PercentualSimplesNacional.ALIQUOTA.value, 2)
        simples_nacional.a_pagar_no_periodo = a_pagar
        inss_salarios = salarios_valor * PercentualSimplesNacional.SALARIOS.value
        inss_pro_labore = pro_labore_valor * PercentualSimplesNacional.PRO_LABORE.value
        inss = round(inss_salarios + inss_pro_labore, 2)
        simples_nacional.inss = inss
        carga = round(a_pagar + inss, 2)
        simples_nacional.carga_tributaria_anual = carga
        simples_nacional.percentual_dos_tributos = round(carga / faturamento_periodo, 4)

        return simples_nacional
