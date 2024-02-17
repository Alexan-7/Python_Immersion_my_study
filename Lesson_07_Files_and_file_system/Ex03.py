# хотим создать файл 'bin-data'
f = open('bin-data', 'wb', buffering=64)
f.write(b'X' * 1200) # бинарная строка
f.close()