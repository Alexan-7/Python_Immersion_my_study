data = [25, -42, 146, 73, -100, 12]
print(list(map(str, data))) # список, где числа - элементы в список как строки
print(max(data, key=lambda x: -x)) # максимальное в отрицательном (меняем знак на противоп-й)
print(*filter(lambda x: not x[0].startswith('__'), globals().items())) # убираем дандер-методы