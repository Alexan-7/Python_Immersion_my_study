my_list = [2, 4, 6, 8, 10, 12]
my_list.insert(2, 555)
print(my_list)
my_list.insert(-2, 13)
print(my_list)
my_list.insert(42, 73) # my_list.append(73)
print(my_list)

mylist = [2, 4, 6, 8, 10, 12, 6]
mylist.remove(6)
print(mylist)
mylist.remove(3) # ValueError: list.remove(x): x not in list
print(mylist)