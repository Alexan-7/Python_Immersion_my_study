"""
Задание №4
- Создайте модуль с функцией внутри.
- Функция получает на вход загадку, список с возможными
вариантами отгадок и количество попыток на угадывание.
- Программа возвращает номер попытки, с которой была
отгадана загадка или ноль, если попытки исчерпаны.
"""

from random import randint

# https://gbcdn.mrgcdn.ru/uploads/record/271643/attachment/c6b58cf4701e5c4acbf8bd55e1828b78.mp4 - 43 мин 30 сек

def func_(start, stop, count):
    num = randint(start, stop + 1)
    i = 0
    while count > i:
        u_num = int(input(f"Угадываем с {count} попыток. Введите число в диапазоне от {start} до {stop}:> "))
        if u_num > num:
            print('Загаданное число меньше!')
        elif u_num < num:
            print('Загаданное число больше!')
        else:
            print('Угадал!')
            return True
        i += 1
    return print('Вы исчерпали попытки! Попробуйте снова.') 

print(func_(1, 11, 3))