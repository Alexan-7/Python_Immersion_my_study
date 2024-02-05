x = [1, 1, 2, 3, 5, 8, 13]
y = [1, 2, 6, 24, 120, 760]
print(f'{len(x)=}\t{len(y)=}')

# создаем генератор из i + j
mult = (i + j for i in x if i % 2 != 0 for j in y if j != i)
res = list(mult)
print(f'{len(res)=}\n{res}')