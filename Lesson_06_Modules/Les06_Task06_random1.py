import random as rnd

START = -100
STOP = 1_000
STEP = 10
data = [2, 4, 6, 8, 42, 73]

print(f'{rnd.randint(START, STOP) = }') # целое число от a до b
print(f'{rnd.uniform(START, STOP) = }') # вещественное число от a до b
print(f'{rnd.choice(data) = }') # случайный элемент последовательности
print(f'{rnd.randrange(START, STOP, STEP) = }') # число из диапазона