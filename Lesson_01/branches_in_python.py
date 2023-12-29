pwd = 'text'
res = input('Input password: ')
if res == pwd:
    print('Access allowed!')
    my_math = int(input('2 + 2 = '))
    if 2 + 2 == my_math:
        print('Вы в нормальном мире')
    else:
        print('Но будьте осторожны')
else:
    print('Access denied.')
print('работа завершена') # не относится к IF