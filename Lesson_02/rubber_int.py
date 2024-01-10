import sys

STEP = 2 ** 16
num = 1
for _ in range(30): # ПОДЧЕРКИВАНИЕ - если нам НЕ НУЖНА переменная, но сам цикл сломается без неё
    print(sys.getsizeof(num), num) # getsizeof(num) - размер объекта в байтах
    num *= STEP

print('\n')
num = 8_769_654_235_767_987 # подчеркивание как разделитель
print(num)