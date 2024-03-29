'''
На вход подается словарь со списком вещей для похода в качестве ключа и их массой max_weight в качестве значения.
Определите какие вещи влезут в рюкзак backpack передав его максимальную грузоподъёмность.
Результат должен быть в виде словаря {предмет:вес} с вещами в рюкзаке и сохранен в переменную backpack.
Достаточно получить один допустимый вариант и сохранить в переменную backpack. Не выводите backpack на экран.
'''

def pack_backpack(items, max_weight):
    fit_items = {}
    for item, weight in items.items():
        if weight <= max_weight:
            fit_items[item] = weight
            max_weight -= weight
    return fit_items


items = {
    "ключи": 0.3,
    "кошелек": 0.2,
    "телефон": 0.5,
    "зажигалка": 0.1
}
max_weight = 1.0

print(pack_backpack(items, max_weight))
