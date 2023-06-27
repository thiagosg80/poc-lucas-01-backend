from enquadramento.enum.enquadramento import Enquadramento
from modelo.enum.data_range import DataRange


class DataYService:
    def get_all(self):
        result = []
        self.__addDesenvolvidos(result)
        self.__addEmDesenvolvimento(result)
        self.__addSubDesenvovidos(result)
        return result

    def __addDesenvolvidos(self, vector):
        for x in range(DataRange.SIZE.value):
            vector.append(Enquadramento.DESENVOLVIDO.value)

    def __addEmDesenvolvimento(self, vector):
        for x in range(DataRange.SIZE.value):
            vector.append(Enquadramento.EM_DESENVOLVIMENTO.value)

    def __addSubDesenvovidos(self, vector):
        for x in range(DataRange.SIZE.value):
            vector.append(Enquadramento.SUB_DESENVOLVIDO.value)
