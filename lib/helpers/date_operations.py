from datetime import datetime

def str_from_date(datetime_obj: datetime) -> str:
    return datetime.strftime(datetime_obj, '%Y-%m-%dT%H:%M:%S.%fZ')

def date_from_str(datetime_str: str) -> datetime:
    return datetime.strptime(datetime_str, '%Y-%m-%dT%H:%M:%S.%fZ')
