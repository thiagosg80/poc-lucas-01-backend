from datetime import datetime

from analise.enum.date_format_br import DateFormatBr


def get_date_br(datetime_input: datetime) -> str:
    return datetime_input.strftime(DateFormatBr.DIA_MES_ANO.value)
