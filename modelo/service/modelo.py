from sklearn.metrics import accuracy_score
from sklearn.svm import LinearSVC
from modelo.service.data_x import DataXService
from modelo.service.data_y import DataYService
from sklearn.model_selection import train_test_split


class ModeloService:
    modeloInstance = LinearSVC(max_iter=200*1000)

    def predict(self, pib, idh, rp) -> str:
        input_params = [int(pib), int(idh), int(rp)]
        return self.modeloInstance.predict([input_params])[0]

    def fit(self):
        x = DataXService().get_all()
        y = DataYService().get_all()
        training_x, test_x, training_y, test_y = train_test_split(x, y)
        self.modeloInstance.fit(training_x, training_y)
        predictions = self.modeloInstance.predict(test_x)
        return accuracy_score(test_y, predictions) * 100
