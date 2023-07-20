from analise.enum.percentual_common import PercentualCommon
from analise.enum.percentual_lucro_real import PercentualLucroReal
from analise.function.get_adicional_irpj import get_adicional_irpj
from analise.function.get_carga_tributaria_anual import get_carga_tributaria_anual
from analise.function.get_icms import get_icms
from analise.function.get_inss import get_inss
from analise.model.lucro_real import LucroReal


class LucroRealService:
    def get(self, faturamento_periodo: float, valor_medio_credito_icms: float, valor_medio_credito_pis: float,
            valor_medio_credito_cofins: float, salarios_valor: float, pro_labore_valor: float,
            lucro_apurado: float) -> LucroReal:

        lucro_real = LucroReal()
        lucro_real.apurado = lucro_apurado
        lucro_real.irpj = lucro_apurado * PercentualCommon.IRPJ.value
        lucro_real.adicional_irpj = get_adicional_irpj(lucro_apurado)
        lucro_real.csll = lucro_apurado * PercentualCommon.CSLL.value
        lucro_real.pis = faturamento_periodo * PercentualLucroReal.PIS.value - valor_medio_credito_pis
        lucro_real.cofins = faturamento_periodo * PercentualLucroReal.COFINS.value - valor_medio_credito_cofins
        lucro_real.icms = get_icms(faturamento_periodo, valor_medio_credito_icms)
        lucro_real.inss = get_inss(salarios_valor, pro_labore_valor)
        carga = get_carga_tributaria_anual(lucro_real)
        lucro_real.carga_tributaria_anual = carga
        lucro_real.percentual_dos_tributos = carga / faturamento_periodo

        return lucro_real
