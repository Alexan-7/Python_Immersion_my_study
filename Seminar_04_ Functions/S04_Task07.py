"""
✔ Функция получает на вход словарь с названием компании в качестве ключа
и списком с доходами и расходами (3-10 чисел) в качестве значения.
✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании
прибыльные, верните истину, а если хотя бы одна убыточная — ложь.
"""

def is_all_profits(companies: dict[str, list[int]]) -> bool:
    temp = []
    for company in companies.values():
        temp.append(sum(company) > 0)
    return all(temp)


if __name__ == "__main__":
    data = {
        "Apple": [42, -73, 12, 85, -15, 3],
        "Yandex": [45, 25, -100, 22, 2, 55],
        "Xiaomi": [-500, 123, 52, 45, 93, 200]
    }
    print(is_all_profits(data))