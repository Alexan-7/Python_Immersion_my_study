my_set = frozenset([3, 4, 1, 2, 5, 6, 1, 7, 2, 7])

print(len(my_set)) # длина коллекции
print(my_set - {1, 2, 3})
print(my_set.union({2, 4, 6, 8}))
print(my_set & {2, 4, 6, 8})
print(my_set.discard(10)) #не вызывает ошибку, но у нас frozenset, поэтому error