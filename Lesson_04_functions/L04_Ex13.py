def mean(args): # принимает на ВХОД значение args
    return sum(args) / len(args)


print(mean([1, 2, 3]))
# print(mean(1, 2, 3)) # mean() takes 1 positional argument but 3 were given
# ошибка при попытке ввести несколько значений


def mean(*args):
    return sum(args) / len(args)


print(mean(*[1, 2, 3]))
print(mean(1, 2, 3))