pi = 3.1415
print(f'Число Пи с точностью два знака: {pi:.2f}')  # вторая f - это float

data = [3245, 44675587, 867975479, 2345, 5643256, 1877]
for item in data:
    print(f'{item:>10}')
    # > - выравн-е по прав. краю, < - выравн-е по лев. краю, ^ - выравн-е по центру

num = 2 * pi * data[1]
print(f'{num = :_}')

a, b, c = input('Введите 3 числа через пробел: ').split()
print(c, b, a)

a, b, c, *_ = input('Введите не менее трех чисел через пробел: ').split()
print(a, b, c, *_)