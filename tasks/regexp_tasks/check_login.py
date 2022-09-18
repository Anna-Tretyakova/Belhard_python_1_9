"""
Написать функцию check_login, которая будет принимать строку и проверять,
что она является логином, который соответствует следующим правилам:
1. Длина от 5 до 20 символов
2. Состоит из букв верхнего и нижнего регистра, цифр, знаков подчеркивания
"""
import re


@staticmethod
def check_login(obj):
    match = re.fullmatch(r"^[a-zA-Z0-9_]{5,20}$", obj)
    print(match[0] if match else "Логин не верен")


print(check_login("Anna_Iva"))
