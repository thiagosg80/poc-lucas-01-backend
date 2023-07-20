from arquivo.function.get_float import get_float


class ProLaboreValueService:
    def get(self, text: str) -> float:
        return get_float('PR..*LABORE ', '\d.*', text)
