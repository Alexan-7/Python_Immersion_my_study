my_list = [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]
print(my_list[2:7:2], 'my_list[2:7:2]')
print(my_list[:7:2], 'my_list[:7:2]') # start = 0 - от начала списка
print(my_list[2::2], 'my_list[2::2]') # stop = 0 - до конца списка
print(my_list[2:7:], 'my_list[2:7:]') # step по умолчанию 1
print(my_list[8:3:-1], 'my_list[8:3:-1]') # движемся справа налево
print(my_list[3::], 'my_list[3::]') # с 3-го элемента
print(my_list[:7:], 'my_list[:7:]') 