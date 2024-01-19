"""
Задание №2
Создайте в переменной data список значений разных типов перечислив их через
запятую внутри квадратных скобок. Для каждого элемента в цикле выведите:
✔ порядковый номер начиная с единицы
✔ значение
✔ адрес в памяти
✔ размер в памяти
✔ хэш объекта
✔ результат проверки на целое число только если он положительный
✔ результат проверки на строку только если он положительный
Добавьте в список повторяющиеся элементы и сравните на результаты.
"""

from  sys import getsizeof, getrefcount

print(getrefcount(1))
data = [3.15164, 'Banana', 1,2, True]
for num, el in enumerate(data, start=1):
    print(f"{num}: {el}: {id(el)}: {getsizeof(el)}: {hash(el)}")
    if type(el) == int and el > 0:
        print(f"Целое и положительное: {el}")
    elif type(el) == str:
        print(f"Строка: {el}")