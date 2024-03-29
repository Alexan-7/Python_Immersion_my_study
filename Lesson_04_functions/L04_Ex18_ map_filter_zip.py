"""map(function, iterable)"""
texts = ["ПрИвеТ", "ЗдорОво", "ДобрыЙ пенЬ!"]
res = map(lambda x: x.lower(), texts)
print(*res)

"""filter(function, iterable)"""
numbers = [42, -73, 1024]
res = tuple(filter(lambda x: x > 0, numbers))
print(res)

"""zip(*iterables, strict=False)"""
names = ["Иван", "Николай", "Петр"]
salaries = [125_000, 96_000, 109_000]
awards = [0.1, 0.25, 0.13, 0.99]
for name, salary, award in zip(names, salaries, awards):
    print(f"{name} заработал {salary:.2f} денег и премию {salary * award:.2f}")