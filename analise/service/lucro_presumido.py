from analise.enum.percentual_common import PercentualCommon
from analise.enum.percentual_lucro_presumido import PercentualLucroPresumido
from analise.function.get_adicional_irpj import get_adicional_irpj
from analise.function.get_carga_tributaria_anual import get_carga_tributaria_anual
from analise.function.get_icms import get_icms
from analise.function.get_inss import get_inss
from analise.model.lucro_presumido import LucroPresumido
from analise.model.presuncao import Presuncao


class LucroPresumidoService:
    def get(self, faturamento_periodo: float, salarios_valor: float, pro_labore_valor: float,
            valor_medio_credito_icms: float) -> LucroPresumido:

        lucro_presumido = LucroPresumido()

        lucro_presumido.presuncao_irpj = self.__get_presuncao(PercentualLucroPresumido.PRESUNCAO_IRPJ.value,
                                                              faturamento_periodo)

        lucro_presumido.presuncao_csll = self.__get_presuncao(PercentualLucroPresumido.PRESUNCAO_CSLL.value,
                                                              faturamento_periodo)

        lucro_presumido.irpj = lucro_presumido.presuncao_irpj.montante * PercentualCommon.IRPJ.value
        lucro_presumido.adicional_irpj = get_adicional_irpj(lucro_presumido.presuncao_irpj.montante)
        lucro_presumido.csll = lucro_presumido.presuncao_csll.montante * PercentualCommon.CSLL.value
        lucro_presumido.pis = faturamento_periodo * PercentualLucroPresumido.PIS.value
        lucro_presumido.cofins = faturamento_periodo * PercentualLucroPresumido.COFINS.value
        lucro_presumido.icms = get_icms(faturamento_periodo, valor_medio_credito_icms)
        lucro_presumido.inss = get_inss(salarios_valor, pro_labore_valor)
        carga_tributaria_anual = get_carga_tributaria_anual(lucro_presumido)
        lucro_presumido.carga_tributaria_anual = carga_tributaria_anual
        lucro_presumido.percentual_dos_tributos = carga_tributaria_anual / faturamento_periodo

        return lucro_presumido

    def __get_presuncao(self, aliquota: float, faturamento: float) -> Presuncao:
        presuncao = Presuncao()
        presuncao.aliquota = aliquota
        presuncao.montante = faturamento * aliquota

        return presuncao
