from analise.enum.percentual_simples_nacional import PercentualSimplesNacional
from analise.function.get_masked_cnae import get_masked_cnae
from analise.model.simples_nacional import SimplesNacional
from analise.model.simples_nacional_encaixe import SimplesNacionalEncaixe
from atividade.service.anexo_simples_nacional import AnexoSimplesNacionalService
from atividade.service.descricao import AtividadeDescricaoService
from atividade.service.faixa_simples_nacional import FaixaSimplesNacionalService


class SimplesNacionalService:
    def get(self, faturamento_periodo: float, salarios_valor: float, pro_labore_valor: float,
            cnaes: str, rbt12: float) -> SimplesNacional:
        simples_nacional = SimplesNacional()
        cnaes_no_mask = cnaes.replace('.', '').replace('-', '')
        simples_nacional.encaixes = self.__get_encaixes(cnaes_no_mask, rbt12)
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

    def __get_encaixes(self, cnaes_input: str, receita_bruta_em_doze_meses: float) -> list:
        anexo_simples_nacional_service = AnexoSimplesNacionalService()
        faixa_simples_nacional_service = FaixaSimplesNacionalService()
        atividade_descricao_service = AtividadeDescricaoService()
        cnaes = cnaes_input.split(',')
        encaixes = []

        [self.__add_encaixe(encaixes, cnae, anexo_simples_nacional_service, faixa_simples_nacional_service,
                            receita_bruta_em_doze_meses, atividade_descricao_service) for cnae in cnaes]

        return encaixes

    def __add_encaixe(self, target: list, cnae: str, anexo_simples_nacional_service: AnexoSimplesNacionalService,
                      faixa_simples_nacional_service: FaixaSimplesNacionalService, receita_bruta_em_doze_meses: float,
                      atividade_descricao_service: AtividadeDescricaoService):

        encaixe = SimplesNacionalEncaixe()
        encaixe.cnae = get_masked_cnae(cnae)
        encaixe.atividade_descricao = atividade_descricao_service.get(cnae)
        anexo = anexo_simples_nacional_service.get(cnae)
        encaixe.anexo = anexo
        faixa_descricao = faixa_simples_nacional_service.get_faixa_key(receita_bruta_em_doze_meses)
        encaixe.faixa_descricao = faixa_descricao
        faixa = faixa_simples_nacional_service.get(anexo, receita_bruta_em_doze_meses)
        encaixe.aliquota = faixa.aliquota
        encaixe.valor_a_deduzir = faixa.valor_a_deduzir
        target.append(encaixe)
