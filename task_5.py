"""
Задание 5.
Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""

import subprocess
import chardet

ping_resurs = [['ping', 'yandex.ru'], ['ping', 'youtube.com']]

for resurs in ping_resurs:
    result = subprocess.run(resurs, stdout=subprocess.PIPE)
    encoding = chardet.detect(result.stdout)['encoding']
    print(result.stdout.decode(encoding))
