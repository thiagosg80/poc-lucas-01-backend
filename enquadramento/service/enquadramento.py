from modelo.service.modelo import ModeloService


class EnquadramentoService:
    def get_enquadramento(self, pib, idh, rp):
        return ModeloService().predict(pib, idh, rp)
