from random import randrange
from modelo.enum.data_range import DataRange


class DataXService:
    def get_all(self):
        result = []
        self.__addDesenvolvidos(result)
        self.__addEmDesenvolvimento(result)
        self.__addSubDesenvovidos(result)
        return result

    def __addDesenvolvidos(self, vector):
        for x in range(DataRange.SIZE.value):
            pib = randrange(21, 40)
            idh = randrange(21, 40)
            rp = randrange(2001, 3000)
            vector.append(self.__get_line(pib, idh, rp))

    def __addEmDesenvolvimento(self, vector):
        for x in range(DataRange.SIZE.value):
            pib = randrange(11, 20)
            idh = randrange(11, 20)
            rp = randrange(1001, 2000)
            vector.append(self.__get_line(pib, idh, rp))

    def __addSubDesenvovidos(self, vector):
        for x in range(DataRange.SIZE.value):
            pib = randrange(1, 10)
            idh = randrange(1, 10)
            rp = randrange(1, 1000)
            vector.append(self.__get_line(pib, idh, rp))

    def __get_line(self, pib, idh, rp):
        return [
            pib,
            idh,
            rp
        ]
