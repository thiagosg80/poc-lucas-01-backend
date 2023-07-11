from analise.enum.percentual_lucro_presumido import PercentualLucroPresumido
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

        irpj = lucro_presumido.presuncao_irpj.montante * PercentualLucroPresumido.IRPJ.value
        lucro_presumido.irpj = irpj
        adicional_irpj = self.__get_adicional_irpj(lucro_presumido.presuncao_irpj.montante)
        lucro_presumido.adicional_irpj = adicional_irpj
        csll = lucro_presumido.presuncao_csll.montante * PercentualLucroPresumido.CSLL.value
        lucro_presumido.csll = csll
        pis = faturamento_periodo * PercentualLucroPresumido.PIS.value
        lucro_presumido.pis = pis
        cofins = faturamento_periodo * PercentualLucroPresumido.COFINS.value
        lucro_presumido.cofins = cofins
        icms = faturamento_periodo * PercentualLucroPresumido.ICMS.value - valor_medio_credito_icms
        lucro_presumido.icms = icms
        inss_salarios = salarios_valor * PercentualLucroPresumido.INSS_SALARIOS.value
        inss_pro_labore= pro_labore_valor * PercentualLucroPresumido.INSS_PRO_LABORE.value
        inss = inss_salarios + inss_pro_labore
        lucro_presumido.inss = inss
        lucro_presumido.valor_medio_credito_icms = valor_medio_credito_icms
        carga_tributaria_anual = irpj + adicional_irpj + csll + pis + cofins + icms + inss
        lucro_presumido.carga_tributaria_anual = carga_tributaria_anual
        lucro_presumido.percentual_dos_tributos = carga_tributaria_anual / faturamento_periodo

        return lucro_presumido

    def __get_presuncao(self, aliquota: float, faturamento: float) -> Presuncao:
        presuncao = Presuncao()
        presuncao.aliquota = aliquota
        presuncao.montante = faturamento * aliquota

        return presuncao

    def __get_adicional_irpj(self, reference: float) -> float:
        corte = 60 * 1000

        return (reference - corte) * PercentualLucroPresumido.ADICIONAL_IRPJ.value if reference > corte else 0
