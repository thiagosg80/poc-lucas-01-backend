import atexit

from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from enquadramento.controller.enquadramento import EnquadramentoController
from modelo.controller.modelo_treinamento import ModeloTreinamentoController
from modelo.service.modelo import ModeloService
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)
CORS(app)
api = Api(app)


api.add_resource(EnquadramentoController, '/enquadramentos/enquadrar')
api.add_resource(ModeloTreinamentoController, '/modelos/treinar')

scheduler = BackgroundScheduler()
scheduler.add_job(func=ModeloService().process_fit, trigger="interval", minutes=1)
scheduler.start()
atexit.register(lambda: scheduler.shutdown())

if __name__ == '__main__':
    app.run(debug=True)
