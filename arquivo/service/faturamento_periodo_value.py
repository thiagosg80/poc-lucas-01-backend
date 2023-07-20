from arquivo.function.get_float import get_float


class FaturamentoPeriodoValueService:
    def get(self, text: str) -> float:
        return get_float('SERVI.OS PRESTADOS ', '\d.*', text)
