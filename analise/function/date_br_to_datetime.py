from datetime import datetime

from analise.enum.date_format_br import DateFormatBr


def get_datetime(date_br: str) -> datetime:
    return datetime.strptime(date_br, DateFormatBr.DIA_MES_ANO.value)
