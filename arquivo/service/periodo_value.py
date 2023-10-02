import re

from analise.function.date_br_to_datetime import get_datetime
from analise.model.periodo_apuracao import PeriodoApuracao


class PeriodoValueService:
    def get(self, text: str) -> PeriodoApuracao:
        match = re.search('Per[ií]odo: .{23}', text)

        return self.__get_periodo_null_safe(match.group()) if match else self.__get_empty_periodo()

    def __get_periodo_null_safe(self, fragment: str) -> PeriodoApuracao:
        start_flag = 'Período: '
        start = len(start_flag)
        end = len(fragment)
        dates_section = fragment[start:end]
        dates = dates_section.split(' - ')
        periodo = PeriodoApuracao()
        periodo.inicio = get_datetime(dates[0])
        periodo.fim = get_datetime(dates[1])

        return periodo

    def __get_empty_periodo(self) -> PeriodoApuracao:
        periodo = PeriodoApuracao()
        periodo.inicio = get_datetime('00/00/0000')
        periodo.fim = get_datetime('00/00/0000')

        return periodo
