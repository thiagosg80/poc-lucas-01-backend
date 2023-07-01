from sklearn.metrics import accuracy_score
from sklearn.svm import LinearSVC

from general.time import Time
from modelo.service.data_x import DataXService
from modelo.service.data_y import DataYService
from sklearn.model_selection import train_test_split


class ModeloService:
    modeloInstance = LinearSVC(max_iter=900*1000)
    pendingFitFlags = []

    def predict(self, pib, idh, rp) -> str:
        input_params = [int(pib), int(idh), int(rp)]
        return self.modeloInstance.predict([input_params])[0]

    def process_fit(self):
        print('Process fit checked at ' + Time().get_today_iso_format())
        if self.pendingFitFlags:
            self.__do_fit()

    def fit(self):
        if not self.pendingFitFlags:
            self.pendingFitFlags.append(Time().get_today_iso_format())

    def __do_fit(self):
        print('Started fit at ' + Time().get_today_iso_format())
        x = DataXService().get_all()
        y = DataYService().get_all()
        training_x, test_x, training_y, test_y = train_test_split(x, y)
        self.modeloInstance.fit(training_x, training_y)
        predictions = self.modeloInstance.predict(test_x)
        score = accuracy_score(test_y, predictions) * 100
        print('End fit at ' + Time().get_today_iso_format() + '. Accuracy Score: ' + str(score))
        self.pendingFitFlags.pop()
