import random as rnd

data = [2, 4, 6, 8, 42, 73]

print(f'{data = }')
rnd.shuffle(data) # перемешиваем коллекцию x in place
print(f'{data = }')

# sample(population, k, *, counts=None) - Выборка в k элементов из population
print(f'{rnd.sample(data, 3) = }')
print(f'{rnd.sample(data, 3, counts=[1, 1, 1, 1, 1, 100]) = }')