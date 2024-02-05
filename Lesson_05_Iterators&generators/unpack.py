a, b, c = input('Введите три символа подряд: ')
print(f'{a = }\t{b = }\t{c = }')

data = ["one", "two", "three", "four", "five", "six", "seven"]
a, b, c, *d = data
print(f'{a=} {b=} {c=} {d=}')

a, b, *c, d = data
print(f'{a=} {b=} {c=} {d=}')

a, *b, c, d = data
print(f'{a=} {b=} {c=} {d=}')

*a, b, c, d = data
print(f'{a=} {b=} {c=} {d=}')

link = 'https://www.pirogov-center.ru/patient/specialists/detail.php?ID=8181'
prefix, *_, suffix = link.split('/')

a = b = c = 0  # Good
a += 42
print(f'{a=} {b=} {c=}')

a = b = c = {1, 2, 3}  # Bad
a.add(42)
print(f'{a=} {b=} {c=}')

a, b, c = 1, 2, 3
print(f'{a=} {b=} {c=}')

t = 1, 2, 3
print(f'{t=}, {type(t)}')

# множественное сравнение
a = b = c = 42
# if a == b and b == c:
if a == b == c:
    print("Full coincidence")

if a < b < c:
    print('b больше a и меньше с')

data = {10, 9, 8, 1, 6, 3}  # множество хеширует
# и упорядочивает в зависимости от хэша
a, b, c, *d, e = data
print(a, b, c, d, e)
