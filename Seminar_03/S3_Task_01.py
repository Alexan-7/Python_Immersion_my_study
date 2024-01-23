"""
Задание №1
✔ Вручную создайте список с целыми числами, которые
повторяются. Получите новый список, который содержит
уникальные (без повтора) элементы исходного списка.
✔ *Подготовьте два решения, короткое и длинное, которое
не использует другие коллекции помимо списков.
"""

lst = [5, 4, 5, 1, 3, 4, 2, 2, 5, 9, 1]
print(lst)
print(list(set(lst)))  # set - множество

new_list = []
lst = [5, 4, 5, 1, 3, 4, 2, 2, 5, 9, 1]
for el in lst:
    if el not in new_list:
        new_list.append(el)
print(sorted(new_list, reverse=True))

# List comprehension на семинаре Дмитрия Читалова
# list = []
# new_list = [for el in lst]
# new_list = [for el in lst if el not in new_list]
# new_list = [new_list.append(el) for el in lst if el not in new_list]

new_list = []
print(list(set(sorted([el for el in lst if el not in new_list], reverse=True))))