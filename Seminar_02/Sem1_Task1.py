"""
Задание №1
Создайте несколько переменных разных типов.
Проверьте к какому типу относятся созданные переменные.
"""

data_list = [4, 3.2878, True, None, 'Hello']
for el in data_list:
    print(type(el))

data_list = [4, 3.2878, True, None, 'Hello']
for i in range(len(data_list)):
    print(i, type(data_list[i]))