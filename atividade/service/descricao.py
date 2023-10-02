class AtividadeDescricaoService:
    map: dict = {}

    def __init__(self):
        self.map = self.__get_map()

    def __get_map(self) -> dict:
        return {
            '1091101': 'Fabricação de produtos de panificação industrial',

            '4729699': 'Comércio varejista de produtos alimentícios em geral ou especializado em produtos '
                       'alimentícios não especificados anteriormente',

            '1091102': 'Fabricação de produtos de padaria e confeitaria com predominância de produção própria',
            '5620104': 'Fornecimento de alimentos preparados preponderantemente para consumo domiciliar'
        }

    def get(self, cnae: str) -> str:
        return self.map[cnae]
