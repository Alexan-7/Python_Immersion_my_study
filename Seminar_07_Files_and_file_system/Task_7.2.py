"""
Напишите функцию, которая генерирует псевдоимена. Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, 
среди которых обязательно должны быть гласные. Полученные имена сохраните в файл
"""

from string import ascii_lowercase
from random import choice, randint

def write_names(filename, lines):
    with open(filename, mode='a', encoding='utf-8') as f:
        for i in range (lines):
            str_name = pseudonames()
            f.write(f"{str_name}\n")

def pseudonames():
    lst = [choice(ascii_lowercase) if i != 2 else choice('aeiouy') for i in range(randint(4, 7))]
    return "".join(lst).capitalize()

if __name__ == "__main__":
    write_names('psdnames.txt', 10)