from analise.model.Input import Input

from arquivo.service.faturamento_periodo_value import FaturamentoPeriodoValueService
from arquivo.service.lucro_apurado_value import LucroApuradoValueService
from arquivo.service.pro_labore_value_service import ProLaboreValueService


class InputService:
    def get(self, text: str):
        input_analise = Input()
        input_analise.faturamento_periodo = FaturamentoPeriodoValueService().get(text)
        input_analise.salarios_valor = 0
        input_analise.pro_labore_valor = ProLaboreValueService().get(text)
        input_analise.vendas = 0
        input_analise.compras_mp = 0
        input_analise.despesa_com_folha = 0
        input_analise.outras_despesas = 0
        input_analise.impostos = 0
        input_analise.valor_medio_credito_icms = 0
        input_analise.valor_medio_credito_pis = 0
        input_analise.valor_medio_credito_cofins = 0
        input_analise.lucro_apurado = LucroApuradoValueService().get(text)

        return input_analise
