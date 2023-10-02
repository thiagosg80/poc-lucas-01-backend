class AnexoSimplesNacionalService:
    map: dict = {}

    def __init__(self):
        self.map = self.__get_map()

    def __get_map(self) -> dict:
        return {
            '1091101': 'II',
            '4729699': 'I',
            '1091102': 'I',
            '5620104': 'I'
        }

    def get(self, cnae: str) -> str:
        return self.map[cnae]
