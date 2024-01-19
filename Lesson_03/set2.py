my_set = {3, 4, 1, 5, 6, 1, 7}
my_set.add((9, 10)) # 9 и 10 в скобкох - это кортеж
print(my_set)
# my_ser.add(9, 10) # TypeError, т.к. можно передать 1 эл-т

my_set.remove(5)
print(my_set)

other_set = {1, 4, 53, 34}
new_set = my_set.intersection(other_set) # пересечение
print(f'пересечение {my_set = }\n{other_set = }\n{new_set = }')

new_set2 = my_set & other_set
print(f'{my_set = }\n{other_set = }\n{new_set2 = }')

new_set3 = my_set.union(other_set) # объединение
print(f'объединение {my_set = }\n{other_set = }\n{new_set3 = }')

new_set4 = my_set | other_set # объединение, union()
print(f'{my_set = }\n{other_set = }\n{new_set4 = }')

new_set5 = my_set - other_set # разность
print(f'разность {my_set = }\n{other_set = }\n{new_set5 = }')

new_set6 = my_set.difference(other_set)
print(f'{my_set = }\n{other_set = }\n{new_set6 = }')