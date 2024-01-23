"""
✔ Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение —
кортеж вещей. Ответьте на вопросы:
✔ Какие вещи взяли все три друга
✔ Какие вещи уникальны, есть только у одного друга
✔ Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
✔ Для решения используйте операции с множествами. Код должен расширяться
на любое большее количество друзей.
"""

hike = {'Вася': ('Палатка', 'Котелок', 'Спички', 'Шашлык'),
        'Петя': ('Палатка', 'Котелок', 'Топор', 'Продукты'),
        'Саша': ('Котелок', 'Топор', 'Медикаменты')
}

# Какие вещи взяли все три друга
temp_bag = None
for things in hike.values():
    if not temp_bag:
        temp_bag = set(things)
        continue
    temp_bag = temp_bag.intersection(set(things))
print(temp_bag)

# Какие вещи уникальны, есть только у одного друга
result_uniq = []
for name, things in hike.items():
    temp = set(things)
    temp_o = set()
    for other in hike.values():
        if things == other:
            continue
        temp_o = temp_o.union(set(other))
    temp = temp.difference(temp_o)
    if temp:
        result_uniq.append((name, temp))
print(result_uniq)

# Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
res_empty = []
for name, things in hike.items():
    temp = set(things)
    for other in hike.values():
        if things == other:
            continue
        temp_o = temp_o.intersection(set(other))
    temp = temp_o.difference(temp)
    if temp:
        res_empty.append((name, temp))
print(res_empty)