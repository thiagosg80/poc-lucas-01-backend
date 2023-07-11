from analise.enum.percentual_simples_nacional import PercentualSimplesNacional
from analise.model.simples_nacional import SimplesNacional


class SimplesNacionalService:
    def get(self, faturamento_periodo: float, salarios_valor: float, pro_labore_valor: float) -> SimplesNacional:
        simples_nacional = SimplesNacional()
        simples_nacional.aliquota = PercentualSimplesNacional.ALIQUOTA.value
        a_pagar = faturamento_periodo * PercentualSimplesNacional.ALIQUOTA.value
        simples_nacional.a_pagar_no_periodo = a_pagar
        inss_salarios = salarios_valor * PercentualSimplesNacional.SALARIOS.value
        inss_pro_labore = pro_labore_valor * PercentualSimplesNacional.PRO_LABORE.value
        inss = inss_salarios + inss_pro_labore
        simples_nacional.inss = inss
        carga = a_pagar + inss
        simples_nacional.carga_tributaria_anual = carga
        simples_nacional.percentual_dos_tributos = carga / faturamento_periodo

        return simples_nacional
