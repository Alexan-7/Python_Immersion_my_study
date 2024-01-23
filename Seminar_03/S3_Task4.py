"""
✔ Создайте вручную список с повторяющимися целыми числами.
✔ Сформируйте список с порядковыми номерами
нечётных элементов исходного списка.
✔ Нумерация начинается с единицы
"""

lst = [1, 1, 2, 2, 4, 4, 3, 3, 6, 6, 7, 7]
res = []
for i in range(len(lst)):
    if lst[i] % 2 == 1:
        res.append(i + 1)
print(res)

# List comprehension:
# print(for i in range(len(lst)))
# print(for i in range(len(lst)) if lst[i] % 2 == 1)
print([i + 1 for i in range(len(lst)) if lst[i] % 2 == 1])
