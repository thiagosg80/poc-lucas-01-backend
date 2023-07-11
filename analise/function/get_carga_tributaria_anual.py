from analise.model.lucro import Lucro


def get_carga_tributaria_anual(lucro: Lucro) -> float:
    return lucro.irpj + lucro.adicional_irpj + lucro.csll + lucro.pis + lucro.cofins + lucro.icms + lucro.inss
