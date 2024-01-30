def quadratic_eq(a, b=0, c=0): # когда определяем функцию, пробелы вокруг "=" можно не ставить
    d = b ** 2 - 4 * a * c
    if d > 0:
        return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)  # вернет кортеж
    if d == 0:
        return -b / (2 * a)


print(quadratic_eq(2, -9))
