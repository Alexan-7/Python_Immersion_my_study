"""
✔ Создайте вручную список с повторяющимися элементами.
✔ Удалите из него все элементы, которые встречаются дважды.
"""

lst = [1, 1, 2, 2, 2, 3, 3, 5, 9, 9]

for el_1 in lst:
    count = 0
    for el_2 in lst:
        if el_1 == el_2:
            count += 1
    if count == 2:
        lst.remove(el_1)
        lst.remove(el_1)
print(lst)