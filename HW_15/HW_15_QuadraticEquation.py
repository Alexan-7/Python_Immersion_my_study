"""
Напишите программу, которая решает квадратные уравнения даже если дискриминант отрицательный.
Используйте комплексные числа для извлечения квадратного корня.
"""

import argparse
import logging
from math import sqrt


def quadratic_equation(a, b, c):
    d = b ** 2 - 4 * a * c
    if d > 0:
        x1 = (-b + sqrt(d)) / (2 * a)
        x2 = (-b - sqrt(d)) / (2 * a)
        return (f'Корни уравнения: x1 = {x1:.3f}; x2 = {x2:.3f}')
    elif d == 0:
        x1 = -b / (2 * a)
        return (f'Корень уравнения: x = {x1:.3f}')
    else:
        real = round(-b / (2 * a), 4)
        imaginary = round(sqrt(abs(d)) / (2 * a), 4)
        x1 = complex(real, imaginary)
        x2 = complex(real, -imaginary)
        return (f'Корни уравнения: x1 = {x1}; x2 = {x2}')


if __name__ == '__main__':
    logging.basicConfig(filename='quadratic.log',
                        filemode='a',
                        encoding='utf-8',
                        format='{levelname:<7} - {asctime} строка {lineno:>3d} : {msg}',
                        style='{',
                        level=logging.INFO)
    logger = logging.getLogger(__name__)

    parser = argparse.ArgumentParser(description="Принимаем строку с данными")
    parser.add_argument('-a', type=str, default='3')
    parser.add_argument('-b', type=str, default='7')
    parser.add_argument('-c', type=str, default='-6')

    args = parser.parse_args()

    try:
        a = int(args.a)
    except ValueError as e:
        logger.error(f'Переданные данные: коэффициент a:"{args.a}", {e}')

    try:
        b = int(args.b)
    except ValueError as e:
        logger.error(f'Переданные данные: коэффициент b:"{args.b}", {e}')

    try:
        c = int(args.c)
    except ValueError as e:
        logger.error(f'Переданные данные: коэффициент a:"{args.c}", {e}')

    try:
        res = quadratic_equation(a, b, c)
        logger.info(f'Решение уравнения: {a}x^2 + ({b})x + ({c}) = 0 , {res}')
        print(res)
    except NameError as e:
        logger.error(f'Переданные данные: коэффициенты a:={args.a}, b={args.b}, c={args.c}", ошибка: {e}')
        print('Переданы некорректные данные, см: quadratic.log')

# Тестирование функции quadratic_equation для случая, когда дискриминант больше нуля.
def test_quadratic_equation_positive_discriminant():
    assert quadratic_equation(1, -3, 2) == 'Корни уравнения: x1 = 2.000; x2 = 1.000'

# Тестирование функции quadratic_equation для случая, когда дискриминант равен нулю.
def test_quadratic_equation_zero_discriminant():
    assert quadratic_equation(1, -2, 1) == 'Корень уравнения: x = 1.000'

# Тестирование функции quadratic_equation для случая, когда дискриминант меньше нуля.
def test_quadratic_equation_negative_discriminant():
    assert quadratic_equation(2, 3, 4) == 'Корни уравнения: x1 = (-0.75 + 1j); x2 = (-0.75 - 1j)'

# Тестирование функции quadratic_equation для случая, когда переданы некорректные коэффициенты.
def test_quadratic_equation_invalid_coefficients():
    assert quadratic_equation('a', 2, 3) is None

# Тестирование функции quadratic_equation для случая, когда переданы значения коэффициентов по умолчанию.
def test_quadratic_equation_default_coefficients():
    assert quadratic_equation(-5, 5, 0) == 'Корни уравнения: x1 = 1.000; x2 = 0.000'