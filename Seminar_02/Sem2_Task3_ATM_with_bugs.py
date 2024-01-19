# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

balance = 0
count_add = 0  # счетчик пополнения
count_out = 0  # счетчик снятия

while True:
    if balance > 5_000_000:
        balance -= balance * 0.1
    action = input('Действия: ')
    if action == 'q':
        print('Выходим из банкомата')
        break
    elif action == 'a':
        summ_add = int(input('Сумма: '))
        if summ_add % 50 == 0:
            balance += summ_add
            count_add += 1
            if count_add % 3 == 0:  # После каждой третей операции пополнения или снятия
                balance *= 1.03  # начисляются проценты - 3%
        else:
            print('Некорректная сумма, надо кратно 50')
            continue
    elif action == 'o':
        summ_out = int(input('Сумма: '))
        comission = summ_out * 0.015
        if comission < 30:
            comission = 30
        elif comission > 600:
            comission = 600

        if summ_out + comission > balance:
            print('Недостаточно средств')
        if summ_out > balance:
               if summ_out % 50 == 0:
                    balance -= summ_out

                    count_out += 1
                    if count_out % 3 == 0:  # После каждой третей операции пополнения или снятия
                        balance *= 1.03  # начисляются проценты - 3%
                else:
                    print('Некорректная сумма, надо кратно 50')
                    continue
        print(f'Сумма: {balance}')