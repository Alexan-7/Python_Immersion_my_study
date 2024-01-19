# Напишите программу, которая получает целое число num и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.
# Пример
# На входе:
# num = 255
# На выходе:
# Шестнадцатеричное представление числа: FF
# Проверка результата: 0xff

num = int(input('Введите число в десятичной системе: '))

BASE = 16
hex_digits = "0123456789ABCDEF"
hex_num = ""
test_hex_num = hex(num)

while num > 0:
    remainder = num % BASE
    hex_num = hex_digits[remainder] + hex_num
    num //= BASE
    
print("Шестнадцатеричное представление числа:", hex_num)
print("Проверка результата:", test_hex_num)