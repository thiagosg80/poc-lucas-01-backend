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

        irpj = round(lucro_presumido.presuncao_irpj.montante * PercentualLucroPresumido.IRPJ.value, 2)
        lucro_presumido.irpj = irpj
        adicional_irpj = self.__get_adicional_irpj(lucro_presumido.presuncao_irpj.montante)
        lucro_presumido.adicional_irpj = adicional_irpj
        csll = round(lucro_presumido.presuncao_csll.montante * PercentualLucroPresumido.CSLL.value, 2)
        lucro_presumido.csll = csll
        pis = round(faturamento_periodo * PercentualLucroPresumido.PIS.value, 2)
        lucro_presumido.pis = pis
        cofins = round(faturamento_periodo * PercentualLucroPresumido.COFINS.value, 2)
        lucro_presumido.cofins = cofins
        icms = round(faturamento_periodo * PercentualLucroPresumido.ICMS.value - valor_medio_credito_icms, 2)
        lucro_presumido.icms = icms
        inss_salarios = salarios_valor * PercentualLucroPresumido.INSS_SALARIOS.value
        inss_pro_labore= pro_labore_valor * PercentualLucroPresumido.INSS_PRO_LABORE.value
        inss = round(inss_salarios + inss_pro_labore, 2)
        lucro_presumido.inss = inss
        lucro_presumido.valor_medio_credito_icms = valor_medio_credito_icms
        carga_tributaria_anual = round(irpj + adicional_irpj + csll + pis + cofins + icms + inss, 2)
        lucro_presumido.carga_tributaria_anual = carga_tributaria_anual
        lucro_presumido.percentual_dos_tributos = round(carga_tributaria_anual / faturamento_periodo, 4)

        return lucro_presumido

    def __get_presuncao(self, aliquota: float, faturamento: float) -> Presuncao:
        presuncao = Presuncao()
        presuncao.aliquota = aliquota
        presuncao.montante = round(faturamento * aliquota, 2)

        return presuncao

    def __get_adicional_irpj(self, reference: float) -> float:
        corte = 60 * 1000

        return round((reference - corte) * PercentualLucroPresumido.ADICIONAL_IRPJ.value, 2) if reference > corte \
            else 0
