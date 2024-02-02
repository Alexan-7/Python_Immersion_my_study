"""
Задание №6
✔ Функция получает на вход список чисел и два индекса.
✔ Вернуть сумму чисел между между переданными индексами.
✔ Если индекс выходит за пределы списка, сумма считается
до конца и/или начала списка
"""

def sum_by_index(nums: list[int | float], start, stop):
    if stop < start:
        stop, start = start, stop
    if start < 0:
        start = 0
    if stop > len(nums) - 1:
        stop = len(nums) - 1
    return sum(nums[start:stop+1]) # срез списка между индексами - и берем сумму от этого
                                   # цикл присутствует внутри логики среза

if __name__ == "__main__":
    print(sum_by_index([1, 2, 3, 4, 5, 6], 0, 2))