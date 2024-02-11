import random as rnd

print(f'{rnd.random() = }')
rnd.seed(42)
state = rnd.getstate() # определяет, как в дальнейшем 
# будет работать генератор случайных чисел
print(f'{state = }')
print(f'{rnd.random() = }')
print(f'{rnd.random() = }')
rnd.setstate(state)
print(f'{rnd.random() = }')
print(f'{rnd.random() = }')