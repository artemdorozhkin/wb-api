from datetime import datetime


def validate_date(date: str):
    try:
        datetime.fromisoformat(date)
    except ValueError:
        raise ValueError(
            "Дата должна быть в формате: 2019-06-20 | 2019-06-20T23:59:59 | 2019-06-20T00:00:00.12345 | 2017-03-25T00:00:00"
        )
