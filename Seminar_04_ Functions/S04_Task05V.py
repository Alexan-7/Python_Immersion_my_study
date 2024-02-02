"""
✔ Функция принимает на вход три списка одинаковой длины:
✔ имена str,
✔ ставка int,
✔ премия str с указанием процентов вида «10.25%».
✔ Вернуть словарь с именем в качестве ключа и суммой
премии в качестве значения.
✔ Сумма рассчитывается как ставка умноженная на процент премии. 
"""

def calculate_bonus(names: list[str], 
                    salaries: list[int], 
                    bonuses: list[str]) -> dict[str, float]:
    result = {}
    for name, salary, bonus in zip(names, salaries, bonuses):
        result[name] = salary * float(bonus[:-1]) / 100
    return result

if __name__ == "__main__":
    imena = ['Борис', 'Александр', 'Василий', 'Максим']
    stavki = [20_000, 40_000, 30_000, 80_000]
    premii = ['12.35%', '10.25%', '7.97%', '11.55%']
    print(calculate_bonus(imena, stavki, premii))