lst = []
for el in range(5): # el - переменная-интератор
    lst.append((el))

lst = [el for el in range(5)]
for el in lst:
    print(el)

# если есть список, то можем пройтись по нему ещё раз
for el in lst:
    print(el)

gen = (el for el in range(5))
for el in gen:
    print(el)

def func():
    return  lst

def fucn():
    yield # вернет объект генератора

def fucn():
    for el in range(5):
        yield el

res = func()
for el in res:
    print(el)