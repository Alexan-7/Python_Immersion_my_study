"""
✔ Напишите функцию, которая принимает строку текста. Вывести функцией каждое слово с новой строки.
✔ Строки нумеруются начиная с единицы.
✔ Слова выводятся отсортированными согласно кодировки Unicode.
✔ Текст выравнивается по правому краю так, чтобы у самого длинного слова был один пробел между ним и номером строки.
"""

text = "Напишите функцию, которая принимает строку текста. Вывести функцией каждое слово с новой строки."

def print_sorted_txt(txt):
    words = txt.lower().split() # переводим в нижний регистр и делим по пробелам
    words = sorted(words) # отсортируем
    max_len = max(len(word) for word in words)

    for i, word in enumerate(words, start=1):
        print(f'{i}, {word:>{max_len}}')

print_sorted_txt(text)

def print_sorted_txt_2(txt):
    for i, word in enumerate(sorted(txt.lower().split()), 1):
        print(f'{i}, {word:>{max(len(word) for word in txt.lower().split())}}')

print_sorted_txt_2(text)