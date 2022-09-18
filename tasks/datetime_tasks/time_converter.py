"""
Написать функцию convert_date, которая будет конвертировать время
из одной временной зоны в другую.

Функция должна принимать 3 аргумента: timestamp, current_zone, new_zone.

Функция должна возвращать время в новой временной зоне.
"""

from datetime import datetime


def convert_date(timestamp, current_zone, new_zone):
    dt = datetime.fromtimestamp(timestamp, new_zone)
    result = datetime.time(dt)
    return result


# Getting the current date and time
dt = datetime.now()
# getting the timestamp
ts = datetime.timestamp(dt)
print(ts)
