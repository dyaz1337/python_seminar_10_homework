"""
Задание 3.
Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки b''
(без encode decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
--- обязательно!!! усложните задачу, "отловив" исключение,
придумайте как это сделать
"""

words = ['attribute', 'класс', 'функция', 'type']

for w in words:
    temp = bytes(w, 'UTF-8')
    try:
        if len(w) != len(temp):
            raise TypeError
    except TypeError:
        print(f"{w} cannot be encoded as bytes")
    else:
        print(f"{w} can be encoded as bytes: {temp}")
