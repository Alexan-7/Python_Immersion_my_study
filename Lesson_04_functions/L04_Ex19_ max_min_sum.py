lst_1 = []
lst_2 = [42, 1823, 877]
lst_3 = [("Иван", 125_000), ("Николай", 96_000), ("Петр", 109_000)]

print(max(lst_1, default='empty'))
print(max(*lst_2))
print(max(lst_3, key=lambda x: x[1]))


lst_1 = []
lst_2 = [42, 1823, 877]
lst_3 = [("Иван", 125_000), ("Николай", 96_000), ("Петр", 109_000)]

print(min(lst_1, default='empty'))
print(min(*lst_2))
print(min(lst_3, key=lambda x: x[1]))


my_list = [42, 1823, 200]

print(sum(my_list))
print(sum(my_list, start=1024)) # просуммировать все элементы и сложить их со start