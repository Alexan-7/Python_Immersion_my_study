def pos_only_arg(arg, /):
    """пример только позиционной функции"""
    print(arg) # Принтим для примера, а не для привычки

    pos_only_arg(42)
    pos_only_arg(arg=42)