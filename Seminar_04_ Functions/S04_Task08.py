"""
✔ Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
✔ Напишите функцию, которая при запуске заменяет содержимое переменных
оканчивающихся на s (кроме переменной из одной буквы s) на None.
✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце.
"""

def redata_variable():
    for name, value in globals().items():
        if name.endswith("s"):
            globals()[name.replace("s", "")] = value
            globals()[name] = None

if __name__ == "__main__":
    names = 3
    name = 2
    cats = "Cats"
    cat = ''
    redata_variable()
    print(f'{names = } {cats = }')
    print(f'{name = } {cat = }')