from flask_restful import Resource
from flask import request
from enquadramento.service.enquadramento import EnquadramentoService


class EnquadramentoController(Resource):
    def get(self):
        args = request.args
        pib = args.get('pib')
        idh = args.get('idh')
        rp = args.get('rp')

        return {'descricao': EnquadramentoService().get_enquadramento(pib, idh, rp)}
