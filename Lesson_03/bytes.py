text_en = 'Hello, World!'
res = text_en.encode('utf-8')
print(res, type(res))

text_ru = 'Привет, мир!' # по 2 байта на каждый символ
res = text_ru.encode('utf-8')
print(res, type(res))

x = bytes(b'\xd0\x9f\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82') # неизменяемый набор байтов
y = bytearray(b'\xd0\x9f\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82, \xd0\xbc\xd0\xb8\xd1\x80!') # изменяемый
print(f'{x = }\n{y = }')