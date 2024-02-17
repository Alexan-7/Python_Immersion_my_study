# менеджер контекста для работы с несколькими файлами
with (
        open('text_data.txt', 'r+', encoding='utf-8') as f1,
        open('bin-data', 'rb') as f2,
        open('data.txt', 'r', encoding='utf-8', errors='backslashreplace') as f3
        # 'backslashreplace' - чтобы уместиться в рекомедуемые 120 симоволов на строку
):
    print(list(f1))
    print(list(f2))
    print(list(f3))