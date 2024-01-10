data = 42
print(isinstance(data, int))

data = True
print(isinstance(data, int))

data = 3.15
print(isinstance(data, (int, float, complex)))

"""
isinstance(object, classinfo) Принимает на вход объект и класс и возвращает истину, 
если объект является экземпляром прямого или косвенного подкласса (сравнивает)
"""