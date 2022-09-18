"""
Написать функцию add_to_path, которая будет добавлять директорию, в которой находится
переданный файл (путь к файлу) в sys.path
"""
import sys
import pathlib


def add_to_path(file):
    sys.path.extend([
        str(pathlib.Path(__file__).parent.resolve())
    ])
    print(sys.path)


print(add_to_path('C:\\Users\\E-group\\OneDrive\\Рабочий стол\\Python_notes.xls'))
