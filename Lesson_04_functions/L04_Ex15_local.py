"""Локальные переменные"""


def func(y: int) -> int:
    x = 100
    # x += 100
    print(f'In func {x = }') # for demo, but not for habit
    return y + 1


x = 42
print(f'In main {x = }')
z = func(x)
print(f'{x = }\t{z = }')