"""
✔ Напишите функцию, которая генерирует псевдоимена.
✔ Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых обязательно должны быть гласные.
✔ Полученные имена сохраните в файл.
"""

from random import randint, choices

VOWELS = 'аеиоуыэюя'  # гласные русские буквы

def write_random_name(count_names: int):
    count = 0
    str_names = "" # строка, куда будем записывать сгенер. имена
    while count != count_names:
        word = choices(alfabet, k=randint(4, 7))
        if any(item in VOWELS for item in word):
            str_names += ''.join(word).capitalize() + '\n' # чтобы с заглавной буквы
            count += 1
    with open('task7_2.txt', 'a', encoding='utf-8') as f:
        f.write(str_names)

alfabet = ''.join([chr(char) for char in range(ord('а'), ord('я') + 1)]) # русский алфавит
write_random_name(6)