"""
Написать функцию count_words, которая будет считать количество слов в тексте,
с учетом, что в начале могут быть пробелы, в конце могут быть пробелы, между слов
может встречаться больше одного пробела подряд.
"""
import re


def count_words(text: str):
    result = len(re.findall(r'\w+', text))
    print(result)


count_words('Python is the $$ best programming language ')
