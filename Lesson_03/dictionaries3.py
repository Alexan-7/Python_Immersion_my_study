# setdefault() - возвращает значение и добавляет ключ в словарь
my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
spam = my_dict.setdefault('five')
print(f'{spam = }\t{my_dict=}')
eggs = my_dict.setdefault('six', 6)
print(f'{eggs = }\t{my_dict=}')
new_spam = my_dict.setdefault('two')
print(f'{new_spam = }\t{my_dict=}')
new_eggs = my_dict.setdefault('one', 1_000)
print(f'{new_eggs = }\t{my_dict=}')

# возвращает объект-итератор dict_keys
print(my_dict.keys())

for key in my_dict.keys():
    print(key)

# возвращает объект-итератор dict_values
print(my_dict.values())

for value in my_dict.values():
    print(value)