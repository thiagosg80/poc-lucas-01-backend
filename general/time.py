from datetime import datetime


class Time:

    def get_today_iso_format(self):
        return datetime.now().isoformat()
