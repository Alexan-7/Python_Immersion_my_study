name = 'Alex'
age = None # можно заменить значение переменной потом

# динамическая типизация
a = 42
print(id(a))
a = 'Hello world!'
print(id(a))
a = 3.14 / 3
print(id(a))

print(name, age, a, 487, 'text', sep=' {`=^O^=`} ', end='#') # sep= - разделитель
print('any text') # end= - продолжай предыдущую строку

res = input('Print your text: ')
print(f'Твой текст {res}')

age = int(input('Сколько тебе лет? '))

# плохой стиль программирования - с магическими числами
how_old = 18 - age
print(how_old, ' осталось до совершеннолетия')

# надо использоввать константу
ADULT = 18
how_old = ADULT - age
print(how_old, ' осталось до совершеннолетия')