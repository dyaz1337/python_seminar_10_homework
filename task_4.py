"""
Задание 4.
Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""
words = ['разработка', 'администрирование', 'protocol', 'standard']

for word in words:
    word_bytes = word.encode('utf-8')
    print(f'{word} в байтах: {word_bytes}')

    decoded_word = word_bytes.decode('utf-8')
    print(f'Байты {word_bytes} в строку: {decoded_word}\n')

