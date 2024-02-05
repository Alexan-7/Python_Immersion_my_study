x = [1, 1, 2, 3, 5, 8, 13]
y = [1, 2, 6, 24, 120, 760]
print(f'{len(x)=}\t{len(y)=}')

# создаем генератор списка из i + j
res = [i + j for i in x if i % 2 != 0 for j in y if j != i]
print(f'{len(res)=}\n{res}')

# создаем генераторное выражение
mult = (i + j for i in x if i % 2 != 0 for j in y if j != i)
for item in mult:
    print(f'{item = }')

