"""
Задание №4
✔ Создайте генератор чётных чисел от нуля до 100.
✔ Из последовательности исключите числа, сумма цифр которых равна 8.
✔ Решение в одну строку.
"""

# print(*(i for i in range(0, 101, 2) if i % 10 + i // 10 != 8)) # лист компрехеншен
# sum([int(i) for i in str(i).split()])

gen = (i for i in range(0, 1021, 2) if sum ([int(i) for i in str(i)]) != 8)
for el in gen:
    print(el)

# lst = []

# for i in range(0, 101, 2):
#     lst.append([int(i) for i in str(i).split()])
# print(lst)

#    if sum ([int(i) for i in str(i).split()]) != 8: