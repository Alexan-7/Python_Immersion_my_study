# На вход автоматически подаются две строки frac1 и frac2 вида a/b - дробь с числителем и знаменателем. Напишите программу, 
# которая должна возвращать сумму и произведение дробей. Для проверки своего кода используйте модуль fractions.
# Пример
# На входе:
# frac1 = "1/2"
# frac2 = "1/3"
# На выходе:
# Сумма дробей: 5/6
# Произведение дробей: 1/6
# Сумма дробей: 5/6
# Произведение дробей: 1/6

frac1_str = input('Введите первую дробь в виде "a/b": ')
frac2_str = input('Введите вторую дробь в виде "a/b": ')

# преобразовать введенное из строк в числа
numer1, denom1 = map(int, frac1_str.split("/"))
numer2, denom2 = map(int, frac2_str.split("/"))

sum_frac_numers = numer1 * denom2 + numer2 * denom1
sum_frac_denoms = denom1 * denom2
sum_frac = (sum_frac_numers, sum_frac_denoms)

mult_frac_numers = numer1 * numer2
mult_frac_denoms = denom1 * denom2
mult_frac = (mult_frac_numers, mult_frac_denoms)

print(f'Сумма дробей: {sum_frac[0]}/{sum_frac[1]}')
print(f'Произведение дробей: {mult_frac[0]}/{mult_frac[1]}')
print(f'Сумма дробей: {sum_frac[0]}/{sum_frac[1]}')
print(f'Произведение дробей: {mult_frac[0]}/{mult_frac[1]}')