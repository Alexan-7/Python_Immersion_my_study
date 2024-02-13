"""
Задание №3
- Улучшаем задачу 2.
- Добавьте возможность запуска функции “угадайки” из модуля в командной строке терминала.
- Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
- Для преобразования строковых аргументов командной строки в числовые параметры
используйте генераторное выражение.
"""

from sys import argv
from random import randint


def func(argums):
    num = randint(argums[0], argums[1])
    i = 0
    while argums[2] > i:
        u_num = int(
            input(f"Угадываем с {argums[2]} попыток. \
Введите число в диапазоне от {argums[0]} до {argums[1]}:> "))
        if u_num > num:
            print('Загаданное число меньше!')
        elif u_num < num:
            print('Загаданное число больше!')
        else:
            print('Угадал!')
            return True
        i += 1
    return False


argums = [int(el) for el in argv[1:]]
print(func(argums))
