def from_one_to_n(n, data=None):
    if data is None:
        data = [] # создаем после проверки
    for i in range(1, n + 1):
        data.append(i)
    return data

# перекрестных значений НЕТ
new_list = from_one_to_n(5)
print(f'{new_list = }')
other_list = from_one_to_n(7)
print(f'{other_list = }')
other_list_2 = from_one_to_n(10)
print(f'{other_list_2 = }')