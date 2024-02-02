"""
✔ Напишите функцию, которая принимает строку текста.
✔ Сформируйте список с уникальными кодами Unicode каждого
символа введённой строки отсортированный по убыванию.
"""

def sort_char(data):
    # множество из data, чтобы убрать все повторяющиеся символы
    lst = list(set([ord(el) for el in data]))
    res = sorted(lst, reverse=True)
    return res
print(sort_char("чтобы убрать все повторяющиеся символы"))

# решение короче
def sort_char(data):
    # множество из data, чтобы убрать все повторяющиеся символы
    return sorted(list(set([ord(el) for el in data])), reverse=True)
print(sort_char("чтобы убрать все повторяющиеся символы"))