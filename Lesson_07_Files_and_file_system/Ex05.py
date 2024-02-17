# менеджер контекста with
with open('text_data.txt', 'r+', encoding='utf-8') as f:
    print(list(f))
print(f.write('Bye!')) # ValueError: I/O operation on closed file.