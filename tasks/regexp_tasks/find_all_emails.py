"""
Написать функцию find_emails, которая принимает текст и находит в нем
все email вида some@some.some
"""
import re


def find_email(text: str):
    result = re.search(r"^(?=.+[a-zA-Z0-9_])(?=.+[@])(?=.+[a-zA-Z0-9_])(?=.+[.])(?=.+[a-zA-Z0-9_])$", text)
    print(result)


find_email("anna@gmail.com")
