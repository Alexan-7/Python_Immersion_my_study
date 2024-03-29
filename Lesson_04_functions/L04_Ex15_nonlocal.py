def main(a):
    """не локальные переменные"""
    x = 1

    def func(y):
        nonlocal x
        x += 100
        print(f'In func {x = }') # for demo, but not for habit
        return y + 1

    return x + func(a)

x = 42
print(f'In main {x = }')
z = main(x)
print(f'{x = }\t{z = }')